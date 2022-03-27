# P019
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# September, April, June and November each have 30 days.
# January, March, July, October, December each have 31 days.
# February has 28 days, except on leap year days it has 29 days.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# 1 jan 1901, - 31, dec 2000
# 1/1/1901 - 12/31/2000
# 1901 % 400 != 0, 1901 is not a leap year, feb has 28 days.
# 1902 % 4 != 0, 1902 is not a leap year, feb has 28 days.
# 1903 % 4 != 0, 1902 is not a leap year, feb has 28 days.
# 1904 % 4 == 0, 1902 is the first leap year in the given data, feb has 29 days.


def main():
    years = [year for year in range(1901, 2001)]
    months = {1:  'Jan',
              2:  'Feb',
              3:  'Mar',
              4:  'Apr',
              5:  'May',
              6:  'Jun',
              7:  'Jul',
              8:  'Aug',
              9:  'Sep',
              10: 'Oct',
              11: 'Nov',
              12: 'Dec'}

    days = {'Jan': 31,
            'Feb': 28,
            'Mar': 31,
            'Apr': 30,
            'May': 31,
            'Jun': 30,
            'Jul': 31,
            'Aug': 31,
            'Sep': 30,
            'Oct': 31,
            'Nov': 30,
            'Dec': 31}

    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_of_week_idx = 1
    answer = 0

    for year in years:
        if is_leap_year(year):
            days['Feb'] = 29
        else:
            days['Feb'] = 28
        for month in range(1, 13):
            for day in range(1, days[months.get(month)] + 1):
                # print(months[month], day, year, day_of_week[day_of_week_idx])
                if day == 1 and day_of_week_idx == 6:
                    answer += 1
                if day_of_week_idx < 6:
                    day_of_week_idx += 1
                else:
                    day_of_week_idx = 0
    print(answer)  # 171


def is_leap_year(year):
    if year % 4 != 0:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
