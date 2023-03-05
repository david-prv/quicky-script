  
  
<div align="center">
<p>
  <img alt="" height="80" src="https://user-images.githubusercontent.com/66866223/222735306-9871074e-a67a-463b-8233-66372cd32ec8.png">
</p>
</div>
  
  
------------------------------

Conceptional Idea - A QuickyPHP Bootstrap Configuration Scriptlang  

This application will transcompile the QuickyScript code to a QuickyPHP-Code bootstrap, from which you can boot a QuickyPHP app using the configured router behaviour.

## Example

Config:
```
[CNF_NAME]

# Route to Page A
/path/to/route/A/ (GET) <QUALIFIED\CLASSNAME.CALLBACK>

# Route to Page B
/path/to/route/B/ (POST) <QUALIFIED\CLASSNAME.CALLBACK>

# Route to Page C
/path/to/route/C/ (PUT) <QUALIFIED\CLASSNAME.CALLBACK>
```
<details>
  <summary>Compiler Result</summary>
  
  ```php
<?php
/**
 * Compiled by QuickyScript Transcompiler
 * 
 * Started at 2023-03-03, 14:09:06
 *
 * @author      David Dewes <hello@david-dewes.de>
 * @version     1.0
 * @license     MIT
 */

use Quicky\Http\Request;
use Quicky\Http\Response;
use Quicky\App;

$app = App::create();
App::session()->start();

// AUTO GENERATED BOOTSTRAP: CNF_NAME

// rule dump:
// {'path': <QuickyScript.parser.Path object at 0x00000187E57DAA40>, 'method': <QuickyScript.parser.Method object at 0x00000187E5AC92D0>, 'callback': <QuickyScript.parser.Callback object at 0x00000187E5AC9270>}
App::route("GET", "/path/to/route/A/", function (Request $request, Response $response) {
    // invoke callback
    $ufrv = call_user_func(array("QUALIFIED\CLASSNAME", "CALLBACK"), $request, $response);
    if (!$ufrv instanceof Response) {
        return $response;
    }
    return $ufrv;
});


// rule dump:
// {'path': <QuickyScript.parser.Path object at 0x00000187E5AC91B0>, 'method': <QuickyScript.parser.Method object at 0x00000187E5AC9150>, 'callback': <QuickyScript.parser.Callback object at 0x00000187E5AC90F0>}
App::route("POST", "/path/to/route/B/", function (Request $request, Response $response) {
    // invoke callback
    $ufrv = call_user_func(array("QUALIFIED\CLASSNAME", "CALLBACK"), $request, $response);
    if (!$ufrv instanceof Response) {
        return $response;
    }
    return $ufrv;
});


// rule dump:
// {'path': <QuickyScript.parser.Path object at 0x00000187E5AC9030>, 'method': <QuickyScript.parser.Method object at 0x00000187E5AC8FD0>, 'callback': <QuickyScript.parser.Callback object at 0x00000187E5AC8F70>}
App::route("PUT", "/path/to/route/C/", function (Request $request, Response $response) {
    // invoke callback
    $ufrv = call_user_func(array("QUALIFIED\CLASSNAME", "CALLBACK"), $request, $response);
    if (!$ufrv instanceof Response) {
        return $response;
    }
    return $ufrv;
});


return $app;
?>

```
</details>

Usage in QuickyPHP:
```php
require __DIR__ . "/../vendor/autoload.php";

use Quicky\Http\Request;
use Quicky\Http\Response;
use Quicky\App;

$app = require_once __DIR__ . "/config.qcnf.php";
$app->run();
```
