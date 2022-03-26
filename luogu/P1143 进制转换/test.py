# P1143 进制转换 https://www.luogu.com.cn/problem/P1143

from typing import List

a = int(input())
n = int(input(), a)
b = int(input())
table = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
    'F'
]
result: List[str] = []
while n > 0:
    result.append(table[n % b])
    n //= b
print(''.join(reversed(result)))
