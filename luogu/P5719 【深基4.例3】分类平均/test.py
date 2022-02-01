# P5719 【深基4.例3】分类平均 https://www.luogu.com.cn/problem/P5719

n, k = map(int, input().split())

a_sum, a_num, b_sum, b_num = 0, 0, 0, 0

for i in range(1, n + 1):
    if i % k:
        b_sum += i
        b_num += 1
    else:
        a_sum += i
        a_num += 1

print('%.1f %.1f' % (a_sum / a_num, b_sum / b_num))
