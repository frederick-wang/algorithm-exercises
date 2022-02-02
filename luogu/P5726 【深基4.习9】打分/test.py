# P5726 【深基4.习9】打分 https://www.luogu.com.cn/problem/P5726

n = int(input())

scores = map(int, input().split())

print('%.2f' % (sum(sorted(scores)[1:-1]) / (n - 2)))
