# RowArray

A row array is an array in which several rows of a meter can be stored.

## Usage

### Create
The RowArray is imported from RowArray.py. When initialising the array, you must specify the [meter type](Meter.md).

````Python
import RowArray import RowArray

array = RowArray(meter=Meter.ELS)
````

### Add
To add a row, simply call up the `append` function.

````Python
row = ablToRow("example.abl")

array.append(row)
````

If you want to add a list and rows to an array.

````Python
first_row = ablToRow("example1.abl")
second_row = ablToRow("example2.abl")
third_row = ablToRow("example3.abl")

array = RowArray(meter=Meter.ELS)
array.addList([first_row, second_row, third_row])
````

### Deleting
There are 2 functions for removing an element.

#### Pop
Delete using the index.

````Python
array.pop(%index)
````

#### Remove
Delete using the row.
````Python
array.remove(%row)
````

#### AsList
If you need the RowArray as a list of rows.
````Python
list = array.asList()
````


