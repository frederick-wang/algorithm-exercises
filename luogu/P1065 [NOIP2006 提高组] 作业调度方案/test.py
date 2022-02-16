# P1065 [NOIP2006 提高组] 作业调度方案 https://www.luogu.com.cn/problem/P1065

from typing import List

m, n = map(int, input().split())
seq = tuple(map(int, input().split()))
machine_seq_list: List[int] = []
time_seq_list: List[int] = []

for i in range(n):
    machine_seq_list += list(map(int, input().split()))

for i in range(n):
    time_seq_list += list(map(int, input().split()))

TimeLine = List[bool]
machines: List[TimeLine] = [[] * n for _ in range(m)]
workpiece_procedure_idx = [0] * n
workpiece_stop_time = [0] * n


def get_space_interval(machine_idx: int, time_cost: int, min_start: int) -> int:
    for start in range(len(machines[machine_idx]) - time_cost + 1):
        if not True in machines[machine_idx][start:start +
                                             time_cost] and start >= min_start:
            return start
    return -1


for workpiece_num in seq:
    workpiece_idx = workpiece_num - 1
    procedure_idx = workpiece_procedure_idx[workpiece_idx]
    machine_num = machine_seq_list[workpiece_idx * m + procedure_idx]
    machine_idx = machine_num - 1
    time_cost = time_seq_list[workpiece_idx * m + procedure_idx]
    min_start = workpiece_stop_time[workpiece_idx]
    start = get_space_interval(machine_idx, time_cost, min_start)
    if start == -1:
        start = len(machines[machine_idx])
        if min_start <= start:
            machines[machine_idx] = machines[machine_idx] + [True] * time_cost
        else:
            diff = min_start - start
            machines[machine_idx] = machines[machine_idx] + [False] * diff + (
                [True] * time_cost)
            # 后面还要用 start 更新该工件结束时间
            start = min_start
    else:
        machines[machine_idx][start:start + time_cost] = [True] * time_cost

    workpiece_procedure_idx[workpiece_idx] += 1
    workpiece_stop_time[workpiece_idx] = start + time_cost

print(max(map(len, machines)))
