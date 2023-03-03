from QuickyScript import lexer

"""
Abstract Syntax Tree - Example:

QCNF('TEST',
    Rule(Path('/'), Callback('\\Namespace\\Class', 'FirstMethodName')),
    Rule(Path('/about'), Callback('\\Namespace\\Class', 'SecondMethodName')),
    Rule(Path('/faq'), Callback('\\Namespace\\Class', 'ThirdMethodName'))
)
"""

##### AST classes

class QCNF:
    def __init__(self, name, *rules):
        self.name = name

        if (len(rules) <= 0): exit("ERROR: Empty rulesets are not allowed")
        self.rules = rules

    def dump(self) -> str:
        return f"Config '{self.name}' has a ruleset of {len(self.rules)} rules loaded"

class Rule:
    def __init__(self, path, method, callback):
        self.path = path
        self.method = method
        self.callback = callback

class Path:
    def __init__(self, path):
        self.path = path

class Method:
    def __init__(self, methodName = "GET"):
        if methodName.lower() == "get":
            self.methodName = "GET"
        elif methodName.lower() == "post":
            self.methodName = "POST"
        elif methodName.lower() == "put":
            self.methodName = "PUT"
        elif methodName.lower() == "update":
            self.methodName = "UPDATE"
        elif methodName.lower() == "delete":
            self.methodName = "DELETE"
        elif methodName.lower() == "patch":
            self.methodName = "PATCH"
        else:
            exit("ERROR: Unknown method name")

class Callback:
    def __init__(self, className, methodName):
        self.className = className
        self.methodName = methodName

##### Verifier

def isValidNameToken(token: lexer.Token) -> bool:
    t_type = type(token)
    return t_type == lexer.WordToken or t_type == lexer.UScoreToken

def isValidPathToken(token: lexer.Token) -> bool:
    t_type = type(token)
    return t_type == lexer.FSlashToken or t_type == lexer.WordToken

def isValidCallbackToken(token: lexer.Token) -> bool:
    t_type = type(token)
    return (t_type == lexer.LThanToken or
            t_type == lexer.BSlashToken or
            t_type == lexer.WordToken or
            t_type == lexer.UScoreToken or
            t_type == lexer.DotToken or
            t_type == lexer.GThanToken)

##### Sub Parsers

def parseName(lst: list[lexer.Token]) -> (str, list[lexer.Token]):
    tokenStack = lst.copy()
    currentToken = tokenStack.pop(0)
    name = ""
    while isValidNameToken(currentToken) and len(tokenStack) > 0:
        name += currentToken.type
        currentToken = tokenStack.pop(0)
    
    if len(tokenStack) == 0: exit("ERROR: Syntax error in config name declaration")
    if type(currentToken) != lexer.RSquareToken: exit("ERROR: Syntax error in config name declaration")

    return (name, tokenStack)

def parsePath(lst: list[lexer.Token]) -> (Path, list[lexer.Token]):
    tokenStack = lst.copy()
    currentToken = tokenStack.pop(0)
    path = ""
    while isValidPathToken(currentToken) and len(tokenStack) > 0:
        path += currentToken.type
        currentToken = tokenStack.pop(0)

    if len(tokenStack) == 0: exit("ERROR: Rule definition insufficient")
    if type(currentToken) != lexer.LParentToken: exit("ERROR: Missing method in rule definition")

    return (Path(path), [currentToken] + tokenStack)

def parseMethod(lst: list[lexer.Token]) -> (Method, list[lexer.Token]):
    tokenStack = lst.copy()
    methodName = ""
    if len(tokenStack) <= 3: exit("ERROR: Rule definition insufficient")

    currentToken = tokenStack.pop(0)
    if type(currentToken) != lexer.LParentToken: exit("ERROR: Missing method in rule definition")

    currentToken = tokenStack.pop(0)
    if type(currentToken) != lexer.WordToken: exit("ERROR: Syntax error in method definition")
    methodName = currentToken.type.lower()
    
    currentToken = tokenStack.pop(0)
    if type(currentToken) != lexer.RParentToken: exit("ERROR: Syntax error in method definition")

    if type(tokenStack[0]) != lexer.LThanToken: exit("ERROR: Missing callback definition")

    return (Method(methodName), tokenStack)

def parseCallback(lst: list[lexer.Token]) -> (Callback, list[lexer.Token]):
    tokenStack = lst.copy()
    className = ""
    methodName = ""

    if type(tokenStack.pop(0)) != lexer.LThanToken or type(tokenStack[-1]) != lexer.GThanToken:
        exit("ERROR: Syntax error in callback definition")

    currentToken = tokenStack.pop(0)

    # Parse className
    while len(tokenStack) > 0 and isValidCallbackToken(currentToken) and type(currentToken) != lexer.DotToken:
        className += currentToken.type
        currentToken = tokenStack.pop(0)
    
    if type(currentToken) != lexer.DotToken: exit("ERROR: Missing method definition in callback")

    # Parse methodName
    while len(tokenStack) > 0 and isValidCallbackToken(currentToken) and type(currentToken) != lexer.GThanToken:
        methodName += currentToken.type
        currentToken = tokenStack.pop(0)

    if len(tokenStack) > 0: exit("ERROR: Unexpected token stack in callback definition:", tokenStack)

    return (Callback(className, methodName[1:]), tokenStack)

def parseRuleSet(lst: list[lexer.Token]) -> (list[Rule], list[lexer.Token]):
    tokenStack = lst.copy()
    ruleSet = list()
    subTokenList = list()

    # Repeat until all tokens are exhausted
    while len(tokenStack) > 0:
        currentToken = tokenStack.pop(0)

        # Check if rule declaration starts with path
        if not isValidPathToken(currentToken):
            exit(f"ERROR: Expected path declaration, but got '{tokenStack[0]}'")

        # Rule declaration ends with '>'
        # Fill subTokenList
        while type(currentToken) != lexer.GThanToken and len(tokenStack) > 0:
            subTokenList.append(currentToken)
            currentToken = tokenStack.pop(0)
        subTokenList.append(currentToken)

        # Check for terminating symbol
        if type(subTokenList[-1]) != lexer.GThanToken:
            exit(f"ERROR: Invalid rule definition with unexpected token '{subTokenList[-1]}'")
        
        # Parse subTokenList
        path, subTokenList = parsePath(subTokenList)
        method, subTokenList = parseMethod(subTokenList)
        callback, subTokenList = parseCallback(subTokenList)

        if len(subTokenList) > 0: exit("ERROR: Unexpected tokens in rule definition:", subTokenList)

        # Define Rule
        ruleSet.append(Rule(path, method, callback))

    return (ruleSet, tokenStack)

##### Main

def parse(lst: list[lexer.Token]) -> QCNF:
    tokenStack = lst.copy()

    if type(lst[0]) != lexer.LSquareToken:
        exit("ERROR: Syntax error in config name declaration")

    # Parse obligatory framework
    name, tokenStack = parseName(tokenStack[1:])
    rules, tokenStack = parseRuleSet(tokenStack)

    return QCNF(name, *rules)
