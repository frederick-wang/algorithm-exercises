# P4447 [AHOI2018初中组]分组 https://www.luogu.com.cn/problem/P4447

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
groups = [[nums[0]]]

for num in nums[1:]:
    for group in reversed(groups):
        if num - 1 == group[-1]:
            group.append(num)
            break
        elif num > group[-1]:
            groups.append([num])
            break
    else:
        groups.append([num])
print(min(map(len, groups)))
