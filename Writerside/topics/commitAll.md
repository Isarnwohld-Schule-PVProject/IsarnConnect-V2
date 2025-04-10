# commitAll

The commitOnly function is a function of the [IsarnConnection](Installation.md) class.

## Usage

Only one row can be passed to the function.

````Python
first_row = ablToRow("example1.abl")
second_row = ablToRow("example2.abl")
third_row = ablToRow("example3.abl")

array = RowArray(meter=Meter.ELS)
array.append(first_row)
array.append(second_row)
array.append(third_row)

isarn.commitAll(array)
````

If you want to add one Row, it is recommended that you only use the [commitOnly](commitOnly.md) function.