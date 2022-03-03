# P1259 黑白棋子的移动 https://www.luogu.com.cn/problem/P1259
# https://www.luogu.com.cn/record/70492696

N = int(input())
b = ['o'] * N + ['*'] * N + ['-', '-']
j = 2 * N
i = N - 1
output = ''
while i > 3:
    output += f'{"".join(b)}\n'
    b[i:i + 2] = ['-', '-']
    b[j:j + 2] = ['o', '*']
    output += f'{"".join(b)}\n'
    j -= 2
    b[i:i + 2] = ['*', '*']
    b[j:j + 2] = ['-', '-']
    i -= 1
tail = ''.join(b[10:])
output += f'oooo****--{tail}\nooo--***o*{tail}\nooo*o**--*{tail}\no--*o**oo*{tail}\no*o*o*--o*{tail}\n--o*o*o*o*{tail}'
print(output)
