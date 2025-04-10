# csvToRowArray

The csvToRowArray method is used to read in a .csv file and get back a [RowArray](RowArray.md).

## Usage

You can import the method from the same file as the [ablToRow](ablToRow.md) function.

````Python
from methods import csvToRowArray
````

You have to pass 2 parameters to the function, the path to the .csv file and the counter as an enum.

````Python
arrays = csvToRowArray("./csv/DatenELS.csv", Meter.ELS)
````