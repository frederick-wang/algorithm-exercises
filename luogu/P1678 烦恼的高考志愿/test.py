# P1678 烦恼的高考志愿 https://www.luogu.com.cn/problem/P1678

from bisect import bisect_left

M, N = map(int, input().split())
LASTEST = M - 1
m = sorted(map(int, input().split()))


def f(x: int) -> int:
    '''获取学生不满意度

    Args:
        x (int): 学生成绩

    Returns:
        int: 学生不满意度
    '''
    i = min(bisect_left(m, x), LASTEST)
    if m[i] == x:
        return 0
    return min(abs(x - m[i]), abs(x - m[i - 1]))


print(sum(map(f, map(int, input().split()))))
