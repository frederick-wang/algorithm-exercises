# P1428 小鱼比可爱 https://www.luogu.com.cn/problem/P1428

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print(len(list(filter(lambda x: x < a[i], a[:i]))), end=' ')
