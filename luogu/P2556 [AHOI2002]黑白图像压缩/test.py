# P2556 [AHOI2002]黑白图像压缩 https://www.luogu.com.cn/problem/P2556

from typing import List

# 读入数据
raw_input = map(int, input().split())
N = next(raw_input) # 这个 N 实际上之后不会用到
nums = map(lambda x: bin(x)[2:].rjust(8, '0'), raw_input) # 各个读入数字的二进制表示（str 类型）
# 放结果的 list
result: List[int] = []
# 当前片段的颜色
color = ''
# 当前片段的长度
length = 0
for b in nums:
    for c in b:
        if c == color:
            length += 1
        else:
            if color:
                span = int(color + bin(length)[2:].rjust(7, '0'), 2)
                result.append(span)
            color = c
            length = 1
# 最后别忘了把最后一段也加入 result 中
span = int(color + bin(length)[2:].rjust(7, '0'), 2)
result.append(span)
# 将结果合并为一个字符串，输出！
print(' '.join(map(str, result)))
