# P5735 【深基7.例1】距离函数 https://www.luogu.com.cn/problem/P5735

x_1, y_1 = map(float, input().split())
x_2, y_2 = map(float, input().split())
x_3, y_3 = map(float, input().split())

print('%.2f' % ((((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5) +
                (((x_1 - x_3)**2 + (y_1 - y_3)**2)**0.5) +
                (((x_2 - x_3)**2 + (y_2 - y_3)**2)**0.5)))
