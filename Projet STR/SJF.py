def sjf_without_preemption(processes):
    # Sort the processes based on 'Arrival Time' first
    processes = sorted(processes, key=lambda x: x['Arrival Time'])
    # For the rest, sort by 'Burst Time'
    processes[1:] = sorted(processes[1:], key=lambda x: x['Burst Time'])
    current_time, waiting_times = 0, []
    gantt_chart = []
    for p in processes:
        if current_time < p['Arrival Time']:
            gantt_chart.append(('Task No Task', p['Arrival Time'] - current_time))
            current_time = p['Arrival Time']

        waiting_times.append(current_time - p['Arrival Time'])
        # Update Gantt chart with the current process
        gantt_chart.append((f'Task {p["Process"]-1}', p['Burst Time']))
        current_time += p['Burst Time']
        average_waiting_time = sum(waiting_times) / len(processes)
    return waiting_times, average_waiting_time, gantt_chart