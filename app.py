import sys
import time
from QuickyScript import lexer
from QuickyScript import parser

"""
Next:
- Allow numbers for config name
- Allow numbers for callback
- Automatic Code Generation

Future:
- Allow more all relevant symbols for routes (@, *, {, })
- Add parameterized callbacks
"""

if (len(sys.argv) <= 1):
    exit("USAGE: python3 app.py config [config [config [config [...]]]]")

st = time.time()

for config in sys.argv[1:]:
    if config.split(".")[1] != "qcnf":
        exit("ERROR: Provided file is not a Quicky-Config")

    with open(config) as f: s = f.read()
    cnf = parser.parse(lexer.tokenize(s))
    
    print(cnf.dump())

fin = time.time()

delta = fin - st
print(f"\nTook {delta} seconds")
