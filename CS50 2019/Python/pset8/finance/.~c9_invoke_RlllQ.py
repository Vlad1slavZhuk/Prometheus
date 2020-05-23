import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    rows = db.execute("SELECT symbol, SUM(shares) as total_shares FROM history WHERE id = :id GROUP BY symbol HAVING total_shares > 0", id=session["user_id"])
    quotes = {}

    cash = user[0]["cash"]

    total = cash

    for row in rows:
        quotes[row["symbol"]] = lookup(row["symbol"])
        total += (quotes[row["symbol"]]["price"] * row["total_shares"])
    return render_template("index.html", quotes=quotes, rows=rows, total=total, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        share = request.form.get("shares")

        if not symbol:
            return apology("mising symbol")

        if not share:
            return apology("mising shares")

        if not share.isdigit():
            return apology("invalid shares")

        quote = lookup(symbol)

        if quote == None:
            return apology("invalid symbol")

        shares = int(share)

        if shares <= 0:
            return apology("can't buy less than or 0 shares")

        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])

        cash = rows[0]["cash"]
        price = quote["price"]

        total_price = price * shares

        if total_price > cash:
            return apology("can't afford")

        # Book keeping (TODO: should be wrapped with a transaction)
        db.execute("UPDATE users SET cash = cash - :price WHERE id = :id", price=total_price, id=session["user_id"])
        db.execute("INSERT INTO history (id, symbol, shares, price) VALUES(:id, :symbol, :shares, :price)",
                   id=session["user_id"],
                   symbol=symbol,
                   shares=shares,
                   price=price)

        flash("Bought!")

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    if request.method == "GET":
        username = request.args.get("username")
        row = db.execute("SELECT COUNT(id) as count FROM users WHERE username = :username", username=username)

        if len(username) >= 1 and row[0]["count"] == 0:
            return jsonify(True , "200")
        else:
            return jsonify(False, "400")

    return jsonify(False, "400")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    rows = db.execute("SELECT * FROM history WHERE id = :id", id=session["user_id"])

    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        symbol = request.form.get("symbol")

        if not symbol:
            return apology("mising sybmbol")

        quote = lookup(symbol)

        if quote == None:
            return apology("invalid symbol")

        return render_template("quoted.html", name=quote["name"], symbol=quote["symbol"], price=quote["price"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username")

        elif not password:
            return apology("must provide password")

        elif password != confirmation:
            return apology("passwords did not match")


        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        if len(rows) != 1 or rows[0]["username"] == username:
            return apology("username taken")

        hash = generate_password_hash(password)
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=username, hash=hash)

        rows = db.execute("SELECT id FROM users WHERE username = :username", username=username)
        session["user_id"] = rows[0]["id"]
        flash("Registered!")
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("mising sybmbol")

        quote = lookup(symbol)

        if quote == None:
            return apology("invalid symbol")

        if not request.form.get("shares"):
            return apology("mising shares")

        shares = int(request.form.get("shares"))

        if shares <= 0:
            return apology("can't sell less than or 0 shares")

        row = db.execute("SELECT SUM(shares) as total_shares FROM history WHERE id = :id AND symbol = :symbol GROUP BY symbol",
                           id=session["user_id"], symbol=symbol)

        if len(row) != 1 or row[0]["total_shares"] <= 0 or row[0]["total_shares"] < shares:
            return apology("you can't sell less than 0 or more than you own")

        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])

        cash = rows[0]["cash"]

        total_price = quote["price"] * shares

        db.execute("UPDATE users SET cash = cash + :price WHERE id = :id", price=total_price, id=session["user_id"])
        db.execute("INSERT INTO history (id, symbol, shares, price) VALUES(:id, :symbol, :shares, :price)",
                   id=session["user_id"],
                   symbol=symbol,
                   shares=-shares,
                   price=quote["price"])

        flash("Sold!")
        return redirect("/")

    else:
        rows = db.execute("SELECT symbol, SUM(shares) as total_shares FROM history WHERE id = :id GROUP BY symbol HAVING total_shares > 0",
                    id=session["user_id"])

        return render_template("sell.html", rows=rows)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
