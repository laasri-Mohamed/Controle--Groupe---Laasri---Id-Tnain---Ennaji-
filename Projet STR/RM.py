from functools import reduce, cmp_to_key
from math import gcd

from RM_IMPL import TaskType, tasktype_cmp, TaskIns, priority_cmp


def _lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0


def lcm(a):
    return reduce(_lcm, a)


input_tasks = [
    {"Task": 1, "Arrival Time": 0, "Burst Time": 3, "Deadline": 7, "Period": 20},
    {"Task": 2, "Arrival Time": 0, "Burst Time": 2, "Deadline": 4, "Period": 5},
    {"Task": 3, "Arrival Time": 0, "Burst Time": 2, "Deadline": 9, "Period": 10}
]


def rm(input_tasks):
    task_types = []
    tasks = []
    hyperperiod = []
    gantt = []

    for input_task in input_tasks:
        task_types.append(TaskType(
            period=input_task["Period"],
            release=input_task["Arrival Time"],
            execution=input_task["Burst Time"],
            deadline=input_task["Deadline"],
            name=f'Task{input_task["Task"]}'
        ))

    # Calculate hyperperiod
    for task_type in task_types:
        hyperperiod.append(int(task_type.period))
    hyperperiod = lcm(hyperperiod)

    # Sort types rate monotonic
    task_types = sorted(task_types, key=tasktype_cmp)

    # Create task instances
    for i in range(0, hyperperiod):
        for task_type in task_types:
            if (i - task_type.release) % task_type.period == 0 and i >= task_type.release:
                start = i
                end = start + task_type.execution
                priority = task_type.period
                tasks.append(TaskIns(start=start, end=end, priority=priority, name=task_type.name))

    # Check utilization
    utilization = 0
    for task_type in task_types:
        utilization += float(task_type.execution) / float(task_type.period)
    if utilization > 1:
        print(utilization)

    # Simulate clock
    clock_step = 1
    for i in range(0, hyperperiod, clock_step):
        # Fetch possible tasks that can use cpu and sort by priority
        possible = []
        for t in tasks:
            if t.start <= i:
                possible.append(t)
        possible = sorted(possible, key=priority_cmp)

        # Select task with the highest priority
        if len(possible) > 0:
            on_cpu = possible[0]
            gantt.append((on_cpu.name, clock_step))
            if on_cpu.use(clock_step):
                tasks.remove(on_cpu)
        else:
            gantt.append(('No Task', clock_step))
        print("\n")

    print("Gantt chart:", gantt)
    return gantt

