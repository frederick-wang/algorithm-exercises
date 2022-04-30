# P1051 [NOIP2005 提高组] 谁拿了最多奖学金

from typing import Dict

d: Dict[str, int] = {}
N = int(input())
all_scholarship = 0
for _ in range(N):
    raw = input().split()
    scholarship = 0
    name = raw[0]
    avg_grade = int(raw[1])
    review_grade = int(raw[2])
    is_cadre = raw[3] == 'Y'
    is_west = raw[4] == 'Y'
    paper_num = int(raw[5])
    # 院士奖学金
    if avg_grade > 80 and paper_num:
        scholarship += 8000
    if avg_grade > 85:
        # 五四奖学金
        if review_grade > 80:
            scholarship += 4000
        # 西部奖学金
        if is_west:
            scholarship += 1000
    # 成绩优秀奖
    if avg_grade > 90:
        scholarship += 2000
    # 班级贡献奖
    if review_grade > 80 and is_cadre:
        scholarship += 850
    all_scholarship += scholarship
    d[name] = scholarship
first_name = sorted(d.keys(), key=d.__getitem__, reverse=True)[0]
print(first_name)
print(d[first_name])
# 这里不能用 sum(d.values()) 求和，因为有重名情况
print(all_scholarship)
