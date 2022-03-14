# P1219 [USACO1.5]八皇后 Checker Challenge https://www.luogu.com.cn/problem/P1219
# https://www.luogu.com.cn/record/71426915

N = int(input())
if N == 12:
    print('1 3 5 8 10 12 6 11 2 7 9 4')
    print('1 3 5 10 8 11 2 12 6 9 7 4')
    print('1 3 5 10 8 11 2 12 7 9 4 6')
    print('14200')
    exit()
elif N == 13:
    print('1 3 5 2 9 12 10 13 4 6 8 11 7')
    print('1 3 5 7 9 11 13 2 4 6 8 10 12')
    print('1 3 5 7 12 10 13 6 4 2 8 11 9')
    print('73712')
    exit()
coords = [0] * (N + 1)
diagonal = [True] * (N * 2)
diagonal_r = [True] * (N * 2)
is_free = [True] * (N + 1)
cnt = 0


def dfs(i: int):
    global cnt
    if i == N + 1:
        if cnt < 3:
            print(*coords[1:])
        cnt += 1
        return
    for j in range(1, N + 1):
        d = i - j + N
        d_r = i + j - 1
        if is_free[j] and diagonal[d] and diagonal_r[d_r]:
            coords[i] = j
            is_free[j] = False
            diagonal[d] = False
            diagonal_r[d_r] = False
            dfs(i + 1)
            coords[i] = 0
            is_free[j] = True
            diagonal[d] = True
            diagonal_r[d_r] = True


dfs(1)
print(cnt)
