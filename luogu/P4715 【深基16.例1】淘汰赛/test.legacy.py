# P4715 【深基16.例1】淘汰赛 https://www.luogu.com.cn/problem/P4715

n = int(input())
teams = list(enumerate(map(int, input().split())))

for i in range(n - 1, 0, -1):
    for _ in range(2**i):
        t1 = teams.pop(0)
        t2 = teams.pop(0)
        teams.append(t1 if t1[1] > t2[1] else t2)
print(teams[1][0] + 1 if teams[0][1] > teams[1][1] else teams[0][0] + 1)
