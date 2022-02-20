# P1271 【深基9.例1】选举学生会 https://www.luogu.com.cn/problem/P1271

N, M = map(int, input().split())
arr = [0] * (N + 1)
for x in map(int, input().split()):
    arr[x] += 1
print(''.join(f'{i} ' * c for i in range(1, N + 1) if (c := arr[i])))
