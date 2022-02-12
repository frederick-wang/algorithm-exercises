# P1045 [NOIP2003 普及组] 麦森数 https://www.luogu.com.cn/problem/P1045

import math

P = int(input())

digits_num = int(math.log10(2) * P + 1)
last_500_digits = pow(2, P, int('1' + '0' * 500)) - 1
last_500_chars = f'{last_500_digits:0500d}'
print(digits_num)
for i in range(10):
    print(last_500_chars[i * 50:(i + 1) * 50])

# 这种写法会超时，用计算机嗯算是没有前途的
# mersenne_number: int = 2**P - 1

# mersene_number_str = str(mersenne_number)
# print(len(mersene_number_str))
# last_500_chars = mersene_number_str[-500:].rjust(500, '0')
# for i in range(10):
#     print(last_500_chars[i * 50:(i + 1) * 50])
