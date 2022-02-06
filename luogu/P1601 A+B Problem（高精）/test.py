# P1601 A+B Problem（高精） https://www.luogu.com.cn/problem/P1601

a = input().strip()[::-1]
b = input().strip()[::-1]

LEN = max(len(a), len(b))
c_len = LEN + 1
c = [0] * (c_len)

for i in range(c_len - 1):
    a_num = int(a[i]) if i < len(a) else 0
    b_num = int(b[i]) if i < len(b) else 0
    c[i] += a_num + b_num
    if c[i] >= 10:
        c[i + 1] += 1
        c[i] -= 10

print(''.join(map(str, c[::-1])).lstrip('0') or '0')
