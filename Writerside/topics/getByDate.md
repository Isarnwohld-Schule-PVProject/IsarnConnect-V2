# getByDate

The getByDate function is used to get all [Rows](Row.md) with the same date.

## Usage

The date is passed to the function as a datetime object and the meter is passed as a [meter-enum](Meter.md).

A [RowArray](RowArray.md) of all rows that match the date is returned.
````Python
date = datetime(2023, 5, 27, 1, 18, 57)

rows = isarn.getByDate(date, Meter.ELS)
````

> The time is not necessary for this function, but it is recommended to enter one to prevent errors.
{style="warning"}

