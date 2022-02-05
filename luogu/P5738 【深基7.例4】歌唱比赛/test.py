# P5738 【深基7.例4】歌唱比赛 https://www.luogu.com.cn/problem/P5738

n, m = map(int, input().split())

max_score = 0.0
for _ in range(n):
    scores = list(map(int, input().split()))
    scores.remove(max(scores))
    scores.remove(min(scores))
    score = sum(scores) / (m - 2)
    if score > max_score:
        max_score = score
print('%.2f' % max_score)
