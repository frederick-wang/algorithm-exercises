# P4305 [JLOI2011]不重复数字 https://www.luogu.com.cn/problem/P4305

from typing import Dict

T = int(input())

for _ in range(T):
    N = int(input())
    # 要用 Dict 而不是 Set，Dict 在 Python 3.6 后是有序的（按插入顺序），而 Set 是无序的
    d: Dict[str, bool] = {}
    # 不用把 n 转换成 int，可以大大加速
    for n in input().split():
        # 一定不要读一个数就 print 一次，会 TLE，把所有数放到最后一起 print
        # 为了加速，不用检测 n not in d
        # 对 d[n] 重复赋值不会影响元素的顺序，d.keys() 的顺序在元素第一次插入时已经确定
        d[n] = True
    # print(' '.join(d.keys())) 比 print(*d.keys()) 快很多
    print(' '.join(d.keys()))
