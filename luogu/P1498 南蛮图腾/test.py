# P1498 南蛮图腾 https://www.luogu.com.cn/problem/P1498

N = int(input())

result = [' /\\ ', '/__\\']
r = 2
for i in range(N - 1):
    graph = result[:]
    for j in range(r):
        result[j] = ' ' * r + result[j] + ' ' * r
    for g in graph:
        result.append(g * 2)
    r *= 2
print('\n'.join(result))
