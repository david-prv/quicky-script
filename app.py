from QuickyScript import lexer

with open('sample1.qcnf') as f: s = f.read()

print(lexer.tokenize(s))