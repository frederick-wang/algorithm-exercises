# P5721 【深基4.例6】数字直角三角形 https://www.luogu.com.cn/problem/P5721

n = int(input())

line_num = 1

for i in range(1, n * (n + 1) // 2 + 1):
    print('%02d' % i, end='')
    line_num += 1
    if line_num == n + 1:
        print('')
        line_num = 1
        n -= 1
