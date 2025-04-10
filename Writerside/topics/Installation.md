from IsarnConnect.DatabaseType import DatabaseType

# Installation

IsarnConnect was developed with the latest version of Python.



## IsarnConnection

You can easily implement IsarnConnect in your Main method by importing the IsarnConnection from isarn_connection.

```python
from isarn_connection import IsarnConnection

isarn = IsarnConnection("%password", "%username", "%address", 
                             "%port", "%database", DatabaseType.POSTGRE)
```

To make sure that no errors occur, it is recommended to call the `connect` function before sending or receiving data.

```Python
isarn.connect()
```

> The functions available in IsarnConnection can only be used when the connection is up and running.
{style="warning"}

<seealso>
<!--Give some related links to how-to articles-->
</seealso>
