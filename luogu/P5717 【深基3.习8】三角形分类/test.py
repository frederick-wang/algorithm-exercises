# P5717 【深基3.习8】三角形分类 https://www.luogu.com.cn/problem/P5717

a, b, c = sorted(map(int, input().split()))

if a + b <= c:
    print('Not triangle')
    exit()

if a**2 + b**2 == c**2:
    print('Right triangle')

if a**2 + b**2 > c**2:
    print('Acute triangle')

if a**2 + b**2 < c**2:
    print('Obtuse triangle')

if a == b or b == c or a == c:
    print('Isosceles triangle')

if a == b == c:
    print('Equilateral triangle')
