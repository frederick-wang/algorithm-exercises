# P1610 鸿山洞的灯 https://www.luogu.com.cn/problem/P1610

N, DIST = map(int, input().split())
lights = sorted(map(int, input().split()))
last_light = lights[0]
result = 0
for i in range(1, N - 1):
    if lights[i + 1] - last_light <= DIST:
        result += 1
    else:
        last_light = lights[i]
print(result)
