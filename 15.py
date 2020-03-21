# Problem 15
# http://www.pythonchallenge.com/pc/return/uzi.html
# <!-- he ain't the youngest, he is the second -->
# <!-- todo: buy flowers for tomorrow -->

import calendar
begin_year_search, end_year_search = 1016, 1996

leap_years = (year for year in range(begin_year_search, end_year_search, 4) if year % 10 == 6)

for candidate_year in leap_years:
    assert candidate_year % 4 == 0
    if calendar.weekday(year=candidate_year, month=1, day=26) == 0:  # Monday
        print(candidate_year)

# second youngest year is 1756, and "tomorrow" would be January 27, mozarts birthday
