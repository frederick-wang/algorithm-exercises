# P1163 银行贷款 https://www.luogu.com.cn/problem/P1163

raw_input = input().split()
original_money, month_money = map(float, raw_input[:2])
month_num = int(raw_input[2])
rate_ub = (month_num * month_money - original_money) / original_money
rate_lb = 0.0


def check(o: float, m: float, num: int, p: float) -> int:
    for _ in range(num):
        o = o * (1 + p) - m
        if o < 0:
            return -1
    return 1


while rate_ub - rate_lb > 1e-4:
    m = (rate_ub + rate_lb) / 2
    if check(original_money, month_money, month_num, m) > 0:
        rate_ub = m
    else:
        rate_lb = m
print('%.1f' % (rate_lb * 100))
