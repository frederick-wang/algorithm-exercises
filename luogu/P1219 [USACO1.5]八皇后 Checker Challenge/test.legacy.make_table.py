# P1219 [USACO1.5]八皇后 Checker Challenge https://www.luogu.com.cn/problem/P1219

N = int(input())
coords = [0] * (N + 1)
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
        if is_free[j]:
            has_diagonal_piece = False
            m = i
            n = j
            while m and n:
                if coords[m] == n:
                    has_diagonal_piece = True
                    break
                m -= 1
                n -= 1
            m = i
            n = j
            while not has_diagonal_piece and m <= N and n <= N:
                if coords[m] == n:
                    has_diagonal_piece = True
                    break
                m += 1
                n += 1
            m = i
            n = j
            while not has_diagonal_piece and m and n <= N:
                if coords[m] == n:
                    has_diagonal_piece = True
                    break
                m -= 1
                n += 1
            m = i
            n = j
            while not has_diagonal_piece and m <= N and n:
                if coords[m] == n:
                    has_diagonal_piece = True
                    break
                m += 1
                n -= 1
            if has_diagonal_piece:
                continue
            coords[i] = j
            is_free[j] = False
            dfs(i + 1)
            coords[i] = 0
            is_free[j] = True


dfs(1)
print(cnt)
