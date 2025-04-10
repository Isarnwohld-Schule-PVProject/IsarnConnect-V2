# getBetweenDate

The getBetweenDate function is used to return all rows that are in a specific time period.

## Usage

The function is passed 2 datetime objects, one from when and one to when the period is. The meter must also be passed.

````Python
from_date = datetime(2023, 5, 27, 1, 18, 57)
to_date = datetime(2023, 5, 30, 1, 18, 57)

rows = isarn.getBetweenDate(from_date, to_date, Meter.ELS)
````
> In this function, only the year, month and day are queried from the datetime, just as in [getByDate](getByDate.md).