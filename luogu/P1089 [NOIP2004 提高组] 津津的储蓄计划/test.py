# P1089 [NOIP2004 提高组] 津津的储蓄计划 https://www.luogu.com.cn/problem/P1089

savings = 0
holdings = 0

success = True
for i in range(12):
    holdings += 300
    budget = int(input())
    residue = (holdings - budget)
    if residue < 0:
        print(-(i + 1))
        success = False
        break
    to_be_saved = (residue // 100) * 100
    savings += to_be_saved
    holdings -= to_be_saved + budget

if success:
    print(savings * 12 // 10 + holdings)
