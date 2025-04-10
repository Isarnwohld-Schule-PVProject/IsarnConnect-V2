# DatabaseType

The DatabaseType enum includes all supported database drivers.

## Usage

The enum is imported from the DatabaseType.py file.

````Python
from DatabaseType import DatabaseType
````

## Source

````Python
from enum import Enum

class DatabaseType(Enum):
    MYSQL = "mysql"
    POSTGRE = "postgre"

````