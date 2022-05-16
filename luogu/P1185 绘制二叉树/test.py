# P1185 绘制二叉树 https://www.luogu.com.cn/problem/P1185

from math import ceil

M, N = map(int, input().split())
tree = [['o'] * int(2**i) for i in range(M)]  # 每一层有 $2^i$ 个节点
for _ in range(N):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    tree[i][j] = ' '  # 删除节点 (i, j)
    for k in range(i + 1, M):  # 删除 节点 (i, j) 的所有子节点
        num: int = 2**(k - i)
        for l in range(j * num, (j + 1) * num):
            tree[k][l] = ' '
for i in range(M):
    diff_i = M - i  # 倒着数是第 diff_i 层
    if diff_i > 1:  # 倒着数的第 1 层比较特殊，独立处理，这里处理其他层的节点及斜杠打印
        left_space_num: int = 2**(diff_i - 2) * 3 - 1  # 最左侧的节点左侧的空格数
        print(' '.join(
            map(
                lambda x: x.center(left_space_num * 2 + 1, ' '),
                tree[i],
            )))  # 打印第 i 层的所有节点
        line_num = ceil(2**(diff_i - 3) * 3 - 1)  # 斜杠行数，注意倒着数第2层的斜杠行数为 1
        for j in range(line_num):
            slash_left_space_num = left_space_num - j - 1  # 最左侧的斜杠左侧的空格数
            for c_i, c in enumerate(tree[i]):  # 处理当前层各个节点所属的斜杠
                # 如果当前节点存在，则打印斜杠，否则打印空格
                sign_left = '/' if c == 'o' else ' '
                sign_right = '\\' if c == 'o' else ' '
                if tree[i + 1][c_i * 2] == ' ':  # 如果左子节点不存在，则左斜杠打印为空格
                    sign_left = ' '
                if tree[i + 1][c_i * 2 + 1] == ' ':  # 如果右子节点不存在，则右斜杠打印为空格
                    sign_right = ' '
                # 打印当前层第 c_i 个节点 c 所属的斜杠
                print(' ' * slash_left_space_num + sign_left + ' ' *
                      (2 * j + 1) + sign_right + ' ' * slash_left_space_num,
                      end='')
                # 如果 c_i 不是最后一个节点，额外打印一个空格
                if c_i < len(tree[i]) - 1:
                    print(' ', end='')
            print()  # 换行
    else:  # 处理倒着数第 1 层的节点
        for idx, c in enumerate(tree[i]):
            print(c, end='')
            if idx < len(tree[i]) - 1:
                print(' ' if idx % 2 else '   ', end='')
        print()
