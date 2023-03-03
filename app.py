import sys
import time
from QuickyScript import lexer
from QuickyScript import parser
from QuickyScript import compiler

QSCRIPT_FILE_EXT = "qcnf"
QSCRIPT_OUT_FILE_EXT = "php"

"""
Next:
- Allow numbers for config name
- Allow numbers for callback
- Allow multiple callbacks
- Add code optimizer

Future:
- Allow more all relevant symbols for routes (@, *, {, })
- Add parameterized callbacks
"""

if __name__ == "__main__":

    if (len(sys.argv) <= 1):
        exit("USAGE: python3 app.py config [config [config [config [...]]]]")

    st = time.time()

    for config in sys.argv[1:]:
        explode = config.split(".")
        if len(explode) <= 1: exit("ERROR: Provided file has no file extension")
        if explode[1] != QSCRIPT_FILE_EXT:
            exit("ERROR: Provided file is not a Quicky-Config")
        with open(config) as f: s = f.read()

        # parse AST
        cnf = parser.parse(lexer.tokenize(s))
        print(cnf.dump())

        # trans-compile to PHP
        out = config + "." + QSCRIPT_OUT_FILE_EXT
        compiler.compile(cnf, out)
        print(f"Compiled to {out}")

    fin = time.time()
    delta = fin - st

    print(f"\nTook {delta} seconds")
