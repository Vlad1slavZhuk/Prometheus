# hello.py

Example work programm:

```c
$ python hello.py
What is your name?
David
hello, David
```

# mario.py

```py
$ python mario.py
Height: 5
    #
   ##
  ###
 ####
#####

$ python mario.py
Height: 3
  #
 ##
###
```

# mario1.py

```py
$ python mario.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
$ python mario.py
Height: 0
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
$ python mario.py
Height: -5
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
$ python mario.py
Height: -5
Height: five
Height: 40
Height: 24
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

# cash.py

```py
$ python cash.py
Change owed: 0.41
4
$ python cash.py
Change owed: -0.41
Change owed: -0.41
Change owed: foo
Change owed: 0.41
4
```

# credit.py

```py
$ python credit.py
Number: 378282246310005
AMEX
$ python credit.py
Number: 3782-822-463-10005
Number: foo
Number: 378282246310005
AMEX
$ python credit.py
Number: 6176292929
INVALID
```

# caesar.py

```console
$ python caesar.py 1
plaintext:  HELLO
ciphertext: IFMMP
$ python caesar.py 13
plaintext:  hello, world
ciphertext: uryyb, jbeyq
$ python caesar.py 13
plaintext:  be sure to drink your Ovaltine
ciphertext: or fher gb qevax lbhe Binygvar
$ python caesar.py
Usage: python caesar.py k
$ python caesar.py 1 2 3 4 5
Usage: python caesar.py k
```

# vigenere.py

```console
$ python vigenere.py 13
Usage: python vigenere.py k
$ python vigenere.py
Usage: python vigenere.py k
$ python vigenere.py bacon and eggs
Usage: python vigenere.py k
$ python vigenere.py bacon
plaintext: Meet me at the park at eleven am
ciphertext: Negh zf av huf pcfx bt gzrwep oz
```

# bleep.py

Створіть програму, яка цензурує повідомлення, які містять слова, зазначені у списку «заборонених слів».

```py
$ python bleep.py banned.txt
What message would you like to censor?
What the heck
What the ****
$ python bleep.py banned.txt
What message would you like to censor?
gosh darn it
**** **** it
```