# P2433 【深基1-2】小学数学 N 合一 https://www.luogu.com.cn/problem/P2433

from math import sqrt

T = int(input())

if T == 1:
    print('I love Luogu!')
elif T == 2:
    print(6, 4)
elif T == 3:
    print(3)
    print(12)
    print(2)
elif T == 4:
    print('%.6g' % (500 / 3))
elif T == 5:
    print(15)
elif T == 6:
    print('%.6g' % sqrt(6**2 + 9**2))
elif T == 7:
    print(110)
    print(90)
    print(0)
elif T == 8:
    pi = 3.141593
    r = 5
    print('%.6g' % (2 * pi * r))
    print('%.6g' % (pi * r**2))
    print('%.6g' % (4 / 3 * pi * r**3))
elif T == 9:
    print(22)
elif T == 10:
    print(9)
elif T == 11:
    print('%.6g' % (100 / 3))
elif T == 12:
    print(ord('M') - ord('A') + 1)
    print(chr(ord('A') + 18 - 1))
elif T == 13:
    pi = 3.141593
    r1 = 4
    r2 = 10
    v = 4 / 3 * pi * r1**3 + 4 / 3 * pi * r2**3
    a = pow(v, 1 / 3)
    print(int(a))
elif T == 14:
    print(50)
