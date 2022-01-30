# P5705 【深基2.例7】数字反转 https://www.luogu.com.cn/problem/P5705

float_num = input()
int_part, fractional_part = float_num.split('.')
reversed_num = float(fractional_part[::-1] + '.' + int_part[::-1])
print(reversed_num)
