# getBetweenTime

The getBetweenTime function is used to return all rows that are in a specific time period.

## Usage

The function is passed 2 datetime objects, one from when and one to when the period is. The meter must also be passed.

````Python
from_date = datetime(2023, 5, 27, 1, 18, 57)
to_date = datetime(2023, 5, 30, 1, 18, 57)

rows = isarn.getBetweenDate(from_date, to_date, Meter.ELS)
````
> It is important to note that you still have to specify all 6 attributes in the datetime object.
{style="warning"}

> This function only queries the hour, minute and second from the datetime, just like [getByTime](getByTime.md).
