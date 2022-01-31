# P5714 【深基3.例7】肥胖问题 https://www.luogu.com.cn/problem/P5714

m, n = map(float, input().split())

bmi = m / n**2

if bmi < 18.5:
    print('Underweight')
elif bmi < 24:
    print('Normal')
else:
    print('%.6g' % bmi)
    print('Overweight')
