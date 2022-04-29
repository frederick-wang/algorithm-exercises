# P1808 单词分类 https://www.luogu.com.cn/problem/P1808

from typing import Set

N = int(input())
s: Set[str] = {str(sorted(input().strip())) for _ in range(N)}
print(len(s))
