# quicky-script
Conceptional Idea - A QuickyPHP Routing-Configuration Scriptlang

Syntax:
```
[CNF_NAME]

/path/to/route (METHOD) <\QUALIFIED\CLASSNAME.CALLBACK>
/path/to/route (METHOD) <\QUALIFIED\CLASSNAME.CALLBACK>
/path/to/route (METHOD) <\QUALIFIED\CLASSNAME.CALLBACK>
```

Usage:
```php
require __DIR__ . "/../vendor/autoload.php";

use Quicky\Http\Request;
use Quicky\Http\Response;
use Quicky\App;

$app = App::create();

App::use("config", __DIR__ . "/sample1.qcnf");

$app->run();
```
