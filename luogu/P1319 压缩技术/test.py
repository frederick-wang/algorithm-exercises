# P1319 压缩技术 https://www.luogu.com.cn/problem/P1319

raw_input = tuple(map(int, input().split()))
N = raw_input[0]

char_num = 0
num = 0
for i in raw_input[1:]:
    for _ in range(i):
        print(num, end='')
        char_num += 1
        if char_num == N:
            char_num = 0
            print()
    num = 1 - num
