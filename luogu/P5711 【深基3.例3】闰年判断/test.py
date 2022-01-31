# P5711 【深基3.例3】闰年判断 https://www.luogu.com.cn/problem/P5711

year = int(input())

# def is_leap_year(year):  # type: (int) -> bool
#     '''
#     判断一个年份是否为闰年
#     '''
#     return year % 400 == 0 if year % 100 == 0 else year % 4 == 0


def is_leap_year(year):  # type: (int) -> bool
    '''
    判断一个年份是否为闰年
    '''
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


print(int(is_leap_year(year)))
