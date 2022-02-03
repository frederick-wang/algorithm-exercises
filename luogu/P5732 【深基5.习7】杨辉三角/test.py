# P5732 【深基5.习7】杨辉三角 https://www.luogu.com.cn/problem/P5732

n = int(input())

if n <= 0:
    print()
    exit

last_line = [1, 1]
for i in range(n):
    if i == 0:
        print(1)
        continue
    if i == 1:
        print(1, 1)
        continue
    line = [1]
    for j in range(i):
        if j == 0:
            print(1, end='')
            continue
        num = last_line[j] + last_line[j - 1]
        print(' %d' % num, end='')
        line.append(num)
    print(' 1')
    line.append(1)
    last_line = line
