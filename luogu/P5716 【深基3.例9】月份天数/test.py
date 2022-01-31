# P5716 【深基3.例9】月份天数 https://www.luogu.com.cn/problem/P5716

year, month = map(int, input().split())


def is_leap_year(year):  # type: (int) -> bool
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(29 if is_leap_year(year) else 28)
