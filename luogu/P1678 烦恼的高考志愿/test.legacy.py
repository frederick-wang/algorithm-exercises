# P1678 烦恼的高考志愿 https://www.luogu.com.cn/problem/P1678

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
    left = 0
    right = LASTEST
    while left <= right:
        mid = (left + right) // 2
        if m[mid] < x:
            left = mid + 1
        elif m[mid] > x:
            right = mid - 1
        else:
            return 0
    return min(abs(x - m[max(right, 0)]), abs(m[min(left, LASTEST)] - x))


print(sum(map(f, map(int, input().split()))))
