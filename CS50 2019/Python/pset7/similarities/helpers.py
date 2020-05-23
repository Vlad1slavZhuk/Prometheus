from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    setA = set(a.split("\n"))
    setB = set(b.split("\n"))
    list = setA & setB
    return list


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    setA = set(sent_tokenize(a))
    setB = set(sent_tokenize(b))
    list = setA & setB
    return list

def substring_tokenize(text, n):
    substrings = []

    for i in range(len(text) - n + 1):
        substrings.append(text[i:i + n])

    return substrings

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    setA = set(substring_tokenize(a, n))
    setB = set(substring_tokenize(b, n))
    list = setA & setB
    return list
