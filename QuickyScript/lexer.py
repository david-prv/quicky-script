##### Token Typedef

class Token:
    def __init__(self, t_type):
        self.type = t_type

class WordToken(Token):
    def __init__(self, t_type):
        Token.__init__(self, t_type)

##### Bracket Tokens

class LSquareToken(Token):
    def __init__(self, t_type = "["):
        Token.__init__(self, t_type)

class RSquareToken(Token):
    def __init__(self, t_type = "]"):
        Token.__init__(self, t_type)

class LCurlToken(Token):
    def __init__(self, t_type = "{"):
        Token.__init__(self, t_type)

class RCurlToken(Token):
    def __init__(self, t_type = "}"):
        Token.__init__(self, t_type)

class LParentToken(Token):
    def __init__(self, t_type = "("):
        Token.__init__(self, t_type)

class RParentToken(Token):
    def __init__(self, t_type = ")"):
        Token.__init__(self, t_type)

class LThanToken(Token):
    def __init__(self, t_type = "<"):
        Token.__init__(self, t_type)

class GThanToken(Token):
    def __init__(self, t_type = ">"):
        Token.__init__(self, t_type)

##### Special Char Tokens

class FSlashToken(Token):
    def __init__(self, t_type = "/"):
        Token.__init__(self, t_type)

class BSlashToken(Token):
    def __init__(self, t_type = "\\"):
        Token.__init__(self, t_type)

class DotToken(Token):
    def __init__(self, t_type = "."):
        Token.__init__(self, t_type)

class UScoreToken(Token):
    def __init__(self, t_type = "_"):
        Token.__init__(self, t_type)

##### Symbol Translation

symbols = {
    "[": LSquareToken(),
    "]": RSquareToken(),
    "{": LCurlToken(),
    "}": RCurlToken(),
    "(": LParentToken(),
    ")": RParentToken(),
    "<": LThanToken(),
    ">": GThanToken(),
    "/": FSlashToken(),
    "\\": BSlashToken(),
    ".": DotToken(),
    "_": UScoreToken() 
}

##### Main

def tokenize(input: str) -> list[Token]:
    tmp = []
    tokenList = []
    skip = False

    for c in input:
        if skip and c != "\n":
            continue
        
        if c == "#":
            skip = True
            continue

        if c.isalpha():
            tmp.append(c)
        else:
            if len(tmp) > 0:
                tokenList.append(WordToken(''.join(tmp)))
                tmp = []

            if c == "\n":
                skip = False
                continue

            if c == "" or c == " ": continue

            if not c in symbols: exit(f"ERROR: Unknown token '{c}' found - aborted.")

            tokenList.append(symbols[c])

    return tokenList

def dump(lst: list[Token]) -> None:
    for el in lst:
        print(el.__dict__)
