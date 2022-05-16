# P1185 绘制二叉树 https://www.luogu.com.cn/problem/P1185

M, N = map(int, input().split())
tree = [['o'] * 2**i for i in range(M)]
for _ in range(N):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    tree[i][j] = ' '
    for k in range(i + 1, M):
        for l in range(j * 2**(k - i), j * 2**(k - i) + 2**(k - i)):
            tree[k][l] = ' '
for i in range(M):
    diff_i = M - i
    if diff_i >= 2:
        left_space_num = 2**(diff_i - 2) * 3 - 1
        print(' '.join(
            map(
                lambda x: x.center(left_space_num * 2 + 1, ' '),
                tree[i],
            )))
        if diff_i >= 3:
            line_num = 2**(diff_i - 3) * 3 - 1
            for j in range(line_num):
                span = left_space_num - j - 1
                for c_i, c in enumerate(tree[i]):
                    sign_left = '/' if c == 'o' else ' '
                    if tree[i + 1][c_i * 2] == ' ':
                        sign_left = ' '
                    sign_right = '\\' if c == 'o' else ' '
                    if tree[i + 1][c_i * 2 + 1] == ' ':
                        sign_right = ' '
                    print(' ' * span + sign_left + ' ' * (2 * j + 1) +
                          sign_right + ' ' * span,
                          end='')
                    if c_i < len(tree[i]) - 1:
                        print(' ', end='')
                print()
        else:
            for c_i, c in enumerate(tree[i]):
                sign_left = '/' if c == 'o' else ' '
                if tree[i + 1][c_i * 2] == ' ':
                    sign_left = ' '
                sign_right = '\\' if c == 'o' else ' '
                if tree[i + 1][c_i * 2 + 1] == ' ':
                    sign_right = ' '
                print(f' {sign_left} {sign_right} ', end='')
                if c_i < len(tree[i]) - 1:
                    print(' ', end='')
            print()
    else:
        for idx, c in enumerate(tree[i]):
            print(c, end='')
            if idx < len(tree[i]) - 1:
                if idx % 2:
                    print(' ', end='')
                else:
                    print('   ', end='')
        print()
