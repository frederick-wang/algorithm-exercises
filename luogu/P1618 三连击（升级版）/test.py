# P1618 三连击（升级版） https://www.luogu.com.cn/problem/P1618

A, B, C = map(int, input().split())
b = B / A
c = C / A

no_flag = True
for i in range(123, 987):
    j = int(i * b)
    k = int(i * c)
    if k > 987:
        break
    if j * A == i * B and k * A == i * C:
        s = set(str(i) + str(j) + str(k))
        if len(s) == 9 and '0' not in s:
            print(i, j, k)
            no_flag = False

if no_flag:
    print('No!!!')
