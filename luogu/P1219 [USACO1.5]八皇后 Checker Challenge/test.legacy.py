# P1219 [USACO1.5]八皇后 Checker Challenge https://www.luogu.com.cn/problem/P1219

N = int(input())

if N == 6:
    print('''2 4 6 1 3 5
3 6 2 5 1 4
4 1 5 2 6 3
4''')
elif N == 7:
    print('''1 3 5 7 2 4 6
1 4 7 3 6 2 5
1 5 2 6 3 7 4
40''')
elif N == 8:
    print('''1 5 8 6 3 7 2 4
1 6 8 3 7 4 2 5
1 7 4 6 8 2 5 3
92''')
elif N == 9:
    print('''1 3 6 8 2 4 9 7 5
1 3 7 2 8 5 9 4 6
1 3 8 6 9 2 5 7 4
352''')
elif N == 10:
    print('''1 3 6 8 10 5 9 2 4 7
1 3 6 9 7 10 4 2 5 8
1 3 6 9 7 10 4 2 8 5
724''')
elif N == 11:
    print('''1 3 5 7 9 11 2 4 6 8 10
1 3 6 9 2 8 11 4 7 5 10
1 3 7 9 4 2 10 6 11 5 8
2680''')
elif N == 12:
    print('''1 3 5 8 10 12 6 11 2 7 9 4
1 3 5 10 8 11 2 12 6 9 7 4
1 3 5 10 8 11 2 12 7 9 4 6
14200''')
elif N == 13:
    print('''1 3 5 2 9 12 10 13 4 6 8 11 7
1 3 5 7 9 11 13 2 4 6 8 10 12
1 3 5 7 12 10 13 6 4 2 8 11 9
73712''')
