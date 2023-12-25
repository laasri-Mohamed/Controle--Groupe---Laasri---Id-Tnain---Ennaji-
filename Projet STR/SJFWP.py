def sjf_with_preemption(processes):
    processes.sort(key=lambda x: x['Arrival Time'])
    n = len(processes)
    current_time = 0
    remaining_time = [process['Burst Time'] for process in processes]
    completed = 0
    waiting_times = [0] * n
    execution_sequence = []
    gantt_representation = []

    while completed != n:
        shortest = None
        shortest_burst = float('inf')

        for i in range(n):
            if remaining_time[i] > 0 and processes[i]['Arrival Time'] <= current_time:
                if remaining_time[i] < shortest_burst:
                    shortest = i
                    shortest_burst = remaining_time[i]

        if shortest is None:
            execution_sequence.append(("No Task", 1))
            current_time += 1
            continue

        remaining_time[shortest] -= 1
        execution_sequence.append((shortest + 1, 1))

        if remaining_time[shortest] == 0:
            completed += 1
            end_time = current_time + 1
            waiting_times[shortest] = end_time - processes[shortest]['Burst Time'] - processes[shortest]['Arrival Time']

        current_time += 1
######
    current_task = execution_sequence[0][0]
    time_slots = 0

    for task, slots in execution_sequence:
        if task == current_task:
            time_slots += slots
        else:
            gantt_representation.append((f"Task {current_task-1}", time_slots))
            current_task = task
            time_slots = slots

    gantt_representation.append((f"Task {current_task-1}", time_slots))

    average_waiting_time = sum(waiting_times) / n
    return waiting_times, average_waiting_time, gantt_representation