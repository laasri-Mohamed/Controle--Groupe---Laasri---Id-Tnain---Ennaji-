def fcfs(processes):
    # Sort the processes by arrival time
    processes.sort(key=lambda x: x['Arrival Time'])

    # Initialize variables
    current_time = 0
    waiting_times = []  # Store waiting time for each process
    gantt_chart = []  # Store Gantt chart entries

    # Calculate waiting time and Gantt chart for each process
    for process in processes:
        # If the process hasn't arrived yet, update the current time
        if current_time < process['Arrival Time']:
            gantt_chart.append(('Task No Task', process['Arrival Time'] - current_time))
            current_time = process['Arrival Time']

        # Calculate waiting time for the current process
        waiting_time = current_time - process['Arrival Time']
        waiting_times.append(waiting_time)

        # Update Gantt chart with the current process
        gantt_chart.append((f'Task {process["Process"] - 1}', process['Burst Time']))
        current_time += process['Burst Time']

    average_waiting_time = sum(waiting_times) / len(waiting_times)
    return waiting_times, average_waiting_time, gantt_chart