# getByTime

The getByTime function is used to get all [Rows](Row.md) with the same time.

## Usage

The time is passed to the function as a datetime object and the meter is passed as a [meter-enum](Meter.md).

A [RowArray](RowArray.md) of all rows that match the time is returned.
````Python
time = datetime(2023, 5, 27, 1, 18, 57)

rows = isarn.getByTime(time, Meter.ELS)
````

> It is important to note that the date must also be indicated! Otherwise it will not work and an error will occur.
{style="warning"}

