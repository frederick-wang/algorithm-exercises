# P1085 [NOIP2004 普及组] 不高兴的津津 https://www.luogu.com.cn/problem/P1085

t_max_sum = 0
unhappy_day = 0

for i in range(7):
    t_school, t_afterschool = map(int, input().split())
    t_sum = t_school + t_afterschool
    if t_sum > 8 and t_sum > t_max_sum:
        t_max_sum = t_sum
        unhappy_day = i + 1

print(unhappy_day)
