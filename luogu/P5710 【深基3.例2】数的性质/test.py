# P5710 【深基3.例2】数的性质 https://www.luogu.com.cn/problem/P5710

x = int(input())


def is_even(x):  # type: (int) -> bool
    '''
    判断一个数是否为偶数
    '''
    return x % 2 == 0


def is_gt4_and_not_gt12(x):  # type: (int) -> bool
    '''
    判断一个数是否大于4且不大于12
    '''
    return 4 < x <= 12


print(
    int(is_even(x) and is_gt4_and_not_gt12(x)),
    int(is_even(x) or is_gt4_and_not_gt12(x)),
    int(is_gt4_and_not_gt12(x) ^ is_even(x)),
    int(not is_even(x) and not is_gt4_and_not_gt12(x)),
)
