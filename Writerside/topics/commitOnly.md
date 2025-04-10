# commitOnly

The commitOnly function is a function of the [IsarnConnection](Installation.md) class.

## Usage

Only one row can be passed to the function.

````Python
row = ablToRow("example.abl")

isarn.commitOnly(row)
````

> If you want to add several rows, it is recommended to use a [RowArray](RowArray.md) with the [commitAll](commitAll.md) command.
{style="warning"}