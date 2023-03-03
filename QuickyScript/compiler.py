import time
from datetime import date
from QuickyScript import parser

PROLOGUE = """<?php
/**
 * Compiled by QuickyScript Transcompiler
 * 
 * Started at """ + str(date.today()) + ", " + time.strftime("%H:%M:%S", time.localtime())  + """
 *
 * @author      David Dewes <hello@david-dewes.de>
 * @version     1.0
 * @license     MIT
 */

use Quicky\\Http\\Request;
use Quicky\\Http\\Response;
use Quicky\\App;

$app = App::create();
App::session()->start();\n\n"""

EPILOGUE = """
return $app;
?>
"""

##### Generators

def generateName(name: str) -> str:
    return "// AUTO GENERATED BOOTSTRAP: " + name + "\n"

def generateRoute(rule: parser.Rule) -> str:
    return """
// rule dump:
// """ + str(rule.__dict__) + """
App::route(\"""" + rule.method.methodName.upper() + """\", \"""" + rule.path.path + """\", function (Request $request, Response $response) {
    // invoke callback
    $ufrv = call_user_func(array(\"""" + rule.callback.className + """\", \"""" + rule.callback.methodName + """\"), [$request, $response]);
    if (!$ufrv instanceof Response) {
        return $response;
    }
    return $ufrv;
});
"""

##### Main

def compile(cnf: parser.QCNF, outFileName: str) -> None:
    code = PROLOGUE + generateName(cnf.name)
    
    for rule in cnf.rules:
        code += generateRoute(rule) + "\n"
    
    code += EPILOGUE

    fp = open(outFileName, "w")
    fp.write(code)
