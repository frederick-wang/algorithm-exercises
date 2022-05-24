# P1866 编号 https://www.luogu.com.cn/problem/P1866

from sys import stdin

N = int(stdin.readline())
nums = sorted(map(int, stdin.readline().split()))
cnt = 0
ans = 1
for n in nums:
    if (num := n - cnt) > 0:
        ans = (ans * num) % 1000000007
        cnt += 1
    else:
        print(0)
        exit()
print(ans)
