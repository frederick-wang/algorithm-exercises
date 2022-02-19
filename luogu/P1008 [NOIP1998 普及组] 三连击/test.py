# P1008 [NOIP1998 普及组] 三连击 https://www.luogu.com.cn/problem/P1008

for i in range(123, 329):
    j = str(2 * i)
    k = str(3 * i)
    s = set(str(i) + j + k)
    if '0' not in s and len(s) == 9:
        print(i, j, k)
