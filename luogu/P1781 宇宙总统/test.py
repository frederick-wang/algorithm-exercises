# P1781 宇宙总统 https://www.luogu.com.cn/problem/P1781

N = int(input())

l = [(int(input()), i) for i in range(1, N + 1)]
l.sort()
num, i = l.pop()
print(f'{i}\n{num}')
