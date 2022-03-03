# P1228 地毯填补问题 https://www.luogu.com.cn/problem/P1228
# https://www.luogu.com.cn/record/70507580

K = int(input())
X, Y = map(int, input().split())
L = 2**K
templ = '%d %d %d'


def f(x: int, y: int, px: int, py: int, l: int):
    if l == 2:
        if px == x and py == y:
            print(templ % (x + 1, y + 1, 1))
        elif px == x and py == y + 1:
            print(templ % (x + 1, y, 2))
        elif px == x + 1 and py == y:
            print(templ % (x, y + 1, 3))
        else:
            print(templ % (x, y, 4))
        return
    h = l >> 1
    x1 = x + h
    y1 = y + h
    if px < x1 and py < y1:
        print(templ % (x1, y1, 1))
        f(x, y, px, py, h)
        f(x, y1, x1 - 1, y1, h)
        f(x1, y, x1, y1 - 1, h)
        f(x1, y1, x1, y1, h)
    elif px < x1 and py >= y1:
        print(templ % (x1, y1 - 1, 2))
        f(x, y, x1 - 1, y1 - 1, h)
        f(x, y1, px, py, h)
        f(x1, y, x1, y1 - 1, h)
        f(x1, y1, x1, y1, h)
    elif px >= x1 and py < y1:
        print(templ % (x1 - 1, y1, 3))
        f(x, y, x1 - 1, y1 - 1, h)
        f(x, y1, x1 - 1, y1, h)
        f(x1, y, px, py, h)
        f(x1, y1, x1, y1, h)
    else:
        print(templ % (x1 - 1, y1 - 1, 4))
        f(x, y, x1 - 1, y1 - 1, h)
        f(x, y1, x1 - 1, y1, h)
        f(x1, y, x1, y1 - 1, h)
        f(x1, y1, px, py, h)


f(1, 1, X, Y, L)
