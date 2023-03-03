# quicky-script
Conceptional Idea - A QuickyPHP Routing-Configuration Scriptlang

Example Config:
```
[CNF_NAME]

/path/to/route/A/ (GET) <\QUALIFIED\CLASSNAME.CALLBACK>
/path/to/route/B/ (POST) <\QUALIFIED\CLASSNAME.CALLBACK>
/path/to/route/C/ (PUT) <\QUALIFIED\CLASSNAME.CALLBACK>
```
<details>
  <summary>Above config trans-compiled</summary>
  
  ```php
<?php

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
    $ufrv = call_user_func(array("\QUALIFIED\CLASSNAME", "CALLBACK"), [$request, $response]);
    if (!$ufrv instanceof Response) {
        return $response;
    }
    return $ufrv;
});


// rule dump:
// {'path': <QuickyScript.parser.Path object at 0x00000187E5AC91B0>, 'method': <QuickyScript.parser.Method object at 0x00000187E5AC9150>, 'callback': <QuickyScript.parser.Callback object at 0x00000187E5AC90F0>}
App::route("POST", "/path/to/route/B/", function (Request $request, Response $response) {
    // invoke callback
    $ufrv = call_user_func(array("\QUALIFIED\CLASSNAME", "CALLBACK"), [$request, $response]);
    if (!$ufrv instanceof Response) {
        return $response;
    }
    return $ufrv;
});


// rule dump:
// {'path': <QuickyScript.parser.Path object at 0x00000187E5AC9030>, 'method': <QuickyScript.parser.Method object at 0x00000187E5AC8FD0>, 'callback': <QuickyScript.parser.Callback object at 0x00000187E5AC8F70>}
App::route("PUT", "/path/to/route/C/", function (Request $request, Response $response) {
    // invoke callback
    $ufrv = call_user_func(array("\QUALIFIED\CLASSNAME", "CALLBACK"), [$request, $response]);
    if (!$ufrv instanceof Response) {
        return $response;
    }
    return $ufrv;
});


return $app;
?>

```
</details>

Usage:
```php
require __DIR__ . "/../vendor/autoload.php";

use Quicky\Http\Request;
use Quicky\Http\Response;
use Quicky\App;

$app = require_once "sample1.qcnf.php";
$app->run();
```
