# ablToRow

The ablToRow method is used to create an .abl file as a [Row](Row.md) class.

## Usage

To use them, import them from methods.py and enter the path to the .abl file as the path.

```Python
from methods import ablToRow

row = ablToRow("%path")
```

The method converts all codes that correspond to the OBIS format and returns a [Row](Row.md) object matching the .abl file.

