import pandas as pd
import plotly
import streamlit as st
import plotly.figure_factory as ff
from pygments.lexers import go

from FCFS import fcfs
from SJF import sjf_without_preemption
from SJFWP import sjf_with_preemption
from RM import rm
from DM import dm
from EDF import edf

# Function to display the results of an algorithm
def display_algorithm_results(algorithm_results):
    st.subheader(f"{algorithm_results['Algorithm']} Results:")
    st.bar_chart(algorithm_results["gantt_chart"])

def fcfs_page():
    st.subheader("First-Come, First-Served (FCFS)")

    # Input section
    num_processes = st.number_input("Enter the number of processes:", min_value=1, value=3, step=1)

    processes = []
    for i in range(num_processes):
        # Smaller input fields and layout adjustments
        col1, col2 = st.columns(2)

        with col1:
            arrival_time = st.number_input(f"Arrival Time for Process {i + 1}:", min_value=0, value=0, step=1)

        with col2:
            burst_time = st.number_input(f"Burst Time for Process {i + 1}:", min_value=1, value=5, step=1)

        processes.append({"Process": i + 1, "Arrival Time": arrival_time,"Burst Time": burst_time})

    # Display input processes in a table with borders
    st.subheader("Input Processes:")

    # Convert the processes data to a Pandas DataFrame
    df_processes = pd.DataFrame(processes)

    # Display the DataFrame as a table with specified width
    st.dataframe(df_processes, width=700)  # Adjust the width as needed


    # Run FCFS algorithm and display components
    if st.button("Run FCFS Algorithm"):
        a, b, c = fcfs(processes)
        st.text(f"waiting_times: {a}")
        st.text(f"average_waiting_time: {b}")
        st.text(f"gantt_chart: {c}")

        # Create a list to store the Gantt chart data
        gantt_data = []

        # Set a color for all tasks (e.g., blue)
        task_color = 'rgb(0, 0, 255)'

        # Iterate through the gantt_representation and create Gantt chart data
        current_time_slot = 0
        for task, duration in c:
            if task == 'Task No Task' or task == 'No Task':
                current_time_slot += duration
                continue  # Skip Task No Task
            gantt_data.append(
                dict(Task=task, Start=current_time_slot, Finish=current_time_slot + duration, Color=task_color))
            current_time_slot += duration

        # Create a Gantt chart figure
        fig = ff.create_gantt(
            gantt_data,
            show_colorbar=True,
            index_col='Task',
            group_tasks=True,
        )
        # Customize figure layout
        # Extract start and finish times for x-axis ticks
        x_ticks = sorted(set(time for task in gantt_data for time in [task['Start'], task['Finish']]))

        # Convert times to strings displaying only seconds
        x_ticks_str = [str(time % 60) for time in x_ticks]

        fig.update_layout(
            xaxis=dict(
                showgrid=True,  # Show grids on the x-axis
                #range=[0, current_time_slot]
                tickvals = x_ticks,
                ticktext = x_ticks_str,
            ),
            yaxis=dict(
               showgrid=True,  # Show grids on the y-axis
            ),
            title_text='Gantt Chart',
            xaxis_title='Time Slots',
            yaxis_title='Tasks',
            xaxis_type='linear',  # Set x-axis type to category
        )
        # Display the Gantt chart using Streamlit
        st.plotly_chart(fig)
def sjf_page():
    st.subheader("Shortest Job First (SJF) without Preemption")
    # Input section
    num_processes = st.number_input("Enter the number of processes:", min_value=1, value=3, step=1)

    processes = []
    for i in range(num_processes):
        # Smaller input fields and layout adjustments
        col1, col2 = st.columns(2)

        with col1:
            arrival_time = st.number_input(f"Arrival Time for Process {i + 1}:", min_value=0, value=0, step=1)

        with col2:
            burst_time = st.number_input(f"Burst Time for Process {i + 1}:", min_value=1, value=5, step=1)

        processes.append({"Process": i + 1, "Arrival Time": arrival_time,"Burst Time": burst_time})

    # Display input processes in a table with borders
    st.subheader("Input Processes:")

    # Convert the processes data to a Pandas DataFrame
    df_processes = pd.DataFrame(processes)

    # Display the DataFrame as a table with specified width
    st.dataframe(df_processes, width=700)  # Adjust the width as needed

    if st.button("Run SJF Without Preemption Algorithm"):
        a, b, c = sjf_without_preemption(processes)
        st.text(f"waiting_times: {a}")
        st.text(f"average_waiting_time: {b}")
        st.text(f"gantt_chart: {c}")

        # Create a list to store the Gantt chart data
        gantt_data = []

        # Set a color for all tasks (e.g., blue)
        task_color = 'rgb(0, 0, 255)'

        # Iterate through the gantt_representation and create Gantt chart data
        current_time_slot = 0
        for task, duration in c:
            if task == 'Task No Task' or task == 'No Task':
                current_time_slot += duration
                continue  # Skip Task No Task
            gantt_data.append(
                dict(Task=task, Start=current_time_slot, Finish=current_time_slot + duration, Color=task_color))
            current_time_slot += duration

        # Create a Gantt chart figure
        fig = ff.create_gantt(
            gantt_data,
            show_colorbar=True,
            index_col='Task',
            group_tasks=True,
        )
        # Customize figure layout
        # Extract start and finish times for x-axis ticks
        x_ticks = sorted(set(time for task in gantt_data for time in [task['Start'], task['Finish']]))

        # Convert times to strings displaying only seconds
        x_ticks_str = [str(time % 60) for time in x_ticks]

        fig.update_layout(
            xaxis=dict(
                showgrid=True,  # Show grids on the x-axis
                # range=[0, current_time_slot]
                tickvals=x_ticks,
                ticktext=x_ticks_str,
            ),
            yaxis=dict(
                showgrid=True,  # Show grids on the y-axis
            ),
            title_text='Gantt Chart',
            xaxis_title='Time Slots',
            yaxis_title='Tasks',
            xaxis_type='linear',  # Set x-axis type to category
        )
        # Display the Gantt chart using Streamlit
        st.plotly_chart(fig)

def sjf_preemption():
    st.subheader("Shortest Job First (SJF) with Preemption")
    # Input section
    num_processes = st.number_input("Enter the number of processes:", min_value=1, value=3, step=1)

    processes = []
    for i in range(num_processes):
        # Smaller input fields and layout adjustments
        col1, col2 = st.columns(2)

        with col1:
            arrival_time = st.number_input(f"Arrival Time for Process {i + 1}:", min_value=0, value=0, step=1)

        with col2:
            burst_time = st.number_input(f"Burst Time for Process {i + 1}:", min_value=1, value=5, step=1)

        processes.append({"Process": i + 1, "Arrival Time": arrival_time,"Burst Time": burst_time})

    # Display input processes in a table with borders
    st.subheader("Input Processes:")

    # Convert the processes data to a Pandas DataFrame
    df_processes = pd.DataFrame(processes)

    # Display the DataFrame as a table with specified width
    st.dataframe(df_processes, width=700)  # Adjust the width as needed

    if st.button("Run SJF With Preemption Algorithm"):
        a, b, c = sjf_with_preemption(processes)
        st.text(f"waiting_times: {a}")
        st.text(f"average_waiting_time: {b}")
        st.text(f"gantt_chart: {c}")

        # Create a list to store the Gantt chart data
        gantt_data = []

        # Set a color for all tasks (e.g., blue)
        task_color = 'rgb(0, 0, 255)'

        # Iterate through the gantt_representation and create Gantt chart data
        current_time_slot = 0
        for task, duration in c:
            if task == 'Task No Task' or task == 'No Task':
                current_time_slot += duration
                continue  # Skip Task No Task
            gantt_data.append(
                dict(Task=task, Start=current_time_slot, Finish=current_time_slot + duration, Color=task_color))
            current_time_slot += duration

        # Create a Gantt chart figure
        fig = ff.create_gantt(
            gantt_data,
            show_colorbar=True,
            index_col='Task',
            group_tasks=True,
        )
        # Customize figure layout
        # Extract start and finish times for x-axis ticks
        x_ticks = sorted(set(time for task in gantt_data for time in [task['Start'], task['Finish']]))

        # Convert times to strings displaying only seconds
        x_ticks_str = [str(time % 60) for time in x_ticks]

        fig.update_layout(
            xaxis=dict(
                showgrid=True,  # Show grids on the x-axis
                # range=[0, current_time_slot]
                tickvals=x_ticks,
                ticktext=x_ticks_str,
            ),
            yaxis=dict(
                showgrid=True,  # Show grids on the y-axis
            ),
            title_text='Gantt Chart',
            xaxis_title='Time Slots',
            yaxis_title='Tasks',
            xaxis_type='linear',  # Set x-axis type to category
        )
        # Display the Gantt chart using Streamlit
        st.plotly_chart(fig)



def DM_page():
    st.subheader("Deadline Monothonic - DM")

    # Input section
    num_processes = st.number_input("Enter the number of processes:", min_value=1, value=3, step=1)

    processes = []
    for i in range(num_processes):
        # Smaller input fields and layout adjustments
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            arrival_time = st.number_input(f"Arrival Time for Process {i + 1}:", min_value=0, value=0, step=1)

        with col2:
            burst_time = st.number_input(f"Burst Time for Process {i + 1}:", min_value=1, value=1, step=1)

        with col3:
            deadline = st.number_input(f"Deadline for Process {i + 1}:", min_value=0, value=0, step=1)

        with col4:
            period = st.number_input(f"Period for Process {i + 1}:", min_value=1, value=1, step=1)

        processes.append(
            {"Process": i + 1, "Task": i + 1, "Arrival Time": arrival_time, "Burst Time": burst_time,
             "Deadline": deadline,
             "Period": period})

    # Display input processes in a table with borders
    st.subheader("Input Processes:")

    # Convert the processes data to a Pandas DataFrame
    df_processes = pd.DataFrame(processes)

    # Display the DataFrame as a table with specified width
    st.dataframe(df_processes, width=700)  # Adjust the width as needed


    # Run FCFS algorithm and display components
    if st.button("Run DM Algorithm"):
        c = dm(processes)
        st.text(f"gantt_chart: {c}")

        # Create a list to store the Gantt chart data
        gantt_data = []

        # Set a color for all tasks (e.g., blue)
        task_color = 'rgb(0, 0, 255)'

        # Iterate through the gantt_representation and create Gantt chart data
        current_time_slot = 0
        for task, duration in c:
            if task == 'Task No Task' or task == 'No Task':
                current_time_slot += duration
                continue  # Skip Task No Task
            gantt_data.append(
                dict(Task=task, Start=current_time_slot, Finish=current_time_slot + duration, Color=task_color))
            current_time_slot += duration

        # Create a Gantt chart figure
        fig = ff.create_gantt(
            gantt_data,
            show_colorbar=True,
            index_col='Task',
            group_tasks=True,
        )
        # Customize figure layout
        # Extract start and finish times for x-axis ticks
        x_ticks = sorted(set(time for task in gantt_data for time in [task['Start'], task['Finish']]))

        # Convert times to strings displaying only seconds
        x_ticks_str = [str(time % 60) for time in x_ticks]

        fig.update_layout(
            xaxis=dict(
                showgrid=True,  # Show grids on the x-axis
                #range=[0, current_time_slot]
                tickvals = x_ticks,
                ticktext = x_ticks_str,
            ),
            yaxis=dict(
               showgrid=True,  # Show grids on the y-axis
            ),
            title_text='Gantt Chart',
            xaxis_title='Time Slots',
            yaxis_title='Tasks',
            xaxis_type='linear',  # Set x-axis type to category
        )

        # Display the Gantt chart using Streamlit
        st.plotly_chart(fig)

def RM_page():
    st.subheader("Rate Monothonic - RM")

    # Input section
    num_processes = st.number_input("Enter the number of processes:", min_value=1, value=3, step=1)

    processes = []
    for i in range(num_processes):
        # Smaller input fields and layout adjustments
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            arrival_time = st.number_input(f"Arrival Time for Process {i + 1}:", min_value=0, value=0, step=1)

        with col2:
            burst_time = st.number_input(f"Burst Time for Process {i + 1}:", min_value=1, value=1, step=1)

        with col3:
            deadline = st.number_input(f"Deadline for Process {i + 1}:", min_value=0, value=0, step=1)

        with col4:
            period = st.number_input(f"Period for Process {i + 1}:", min_value=1, value=1, step=1)

        processes.append(
            {"Process": i + 1,"Task": i + 1, "Arrival Time": arrival_time, "Burst Time": burst_time, "Deadline": deadline,
             "Period": period})

    # Display input processes in a table with borders
    st.subheader("Input Processes:")

    # Convert the processes data to a Pandas DataFrame
    df_processes = pd.DataFrame(processes)

    # Display the DataFrame as a table with specified width
    st.dataframe(df_processes, width=700)  # Adjust the width as needed

    # Run FCFS algorithm and display components
    if st.button("Run RM Algorithm"):
        c = rm(processes)
        st.text(f"gantt_chart: {c}")

        # Create a list to store the Gantt chart data
        gantt_data = []

        # Set a color for all tasks (e.g., blue)
        task_color = 'rgb(0, 0, 255)'

        # Iterate through the gantt_representation and create Gantt chart data
        current_time_slot = 0
        for task, duration in c:
            if task == 'Task No Task' or task == 'No Task':
                current_time_slot += duration
                continue  # Skip Task No Task
            gantt_data.append(
                dict(Task=task, Start=current_time_slot, Finish=current_time_slot + duration, Color=task_color))
            current_time_slot += duration

        # Create a Gantt chart figure
        fig = ff.create_gantt(
            gantt_data,
            show_colorbar=True,
            index_col='Task',
            group_tasks=True,
        )
        # Customize figure layout
        # Extract start and finish times for x-axis ticks
        x_ticks = sorted(set(time for task in gantt_data for time in [task['Start'], task['Finish']]))

        # Convert times to strings displaying only seconds
        x_ticks_str = [str(time % 60) for time in x_ticks]

        fig.update_layout(
            xaxis=dict(
                showgrid=True,  # Show grids on the x-axis
                # range=[0, current_time_slot]
                tickvals=x_ticks,
                ticktext=x_ticks_str,
            ),
            yaxis=dict(
                showgrid=True,  # Show grids on the y-axis
            ),
            title_text='Gantt Chart',
            xaxis_title='Time Slots',
            yaxis_title='Tasks',
            xaxis_type='linear',  # Set x-axis type to category
        )
        # Display the Gantt chart using Streamlit
        st.plotly_chart(fig)

def EDF_page():
    st.subheader("Earlest Deadline First - EDF")

    # Input section
    num_processes = st.number_input("Enter the number of processes:", min_value=1, value=3, step=1)

    processes = []
    for i in range(num_processes):
        # Smaller input fields and layout adjustments
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            arrival_time = st.number_input(f"Arrival Time for Process {i + 1}:", min_value=0, value=0, step=1)

        with col2:
            burst_time = st.number_input(f"Burst Time for Process {i + 1}:", min_value=1, value=1, step=1)

        with col3:
            deadline = st.number_input(f"Deadline for Process {i + 1}:", min_value=0, value=0, step=1)

        with col4:
            period = st.number_input(f"Period for Process {i + 1}:", min_value=1, value=1, step=1)

        processes.append(
            {"Process": i + 1,"Task": i + 1, "Arrival Time": arrival_time, "Burst Time": burst_time, "Deadline": deadline,
             "Period": period})

    # Display input processes in a table with borders
    st.subheader("Input Processes:")

    # Convert the processes data to a Pandas DataFrame
    df_processes = pd.DataFrame(processes)

    # Display the DataFrame as a table with specified width
    st.dataframe(df_processes, width=700)  # Adjust the width as needed

    # Run FCFS algorithm and display components
    if st.button("Run EDF Algorithm"):
        c = edf(processes)
        st.text(f"gantt_chart: {c}")

        # Create a list to store the Gantt chart data
        gantt_data = []

        # Set a color for all tasks (e.g., blue)
        task_color = 'rgb(0, 0, 255)'

        # Iterate through the gantt_representation and create Gantt chart data
        current_time_slot = 0
        for task, duration in c:
            if task == 'Task No Task' or task == 'No Task':
                current_time_slot += duration
                continue  # Skip Task No Task
            gantt_data.append(
                dict(Task=task, Start=current_time_slot, Finish=current_time_slot + duration, Color=task_color))
            current_time_slot += duration

        # Create a Gantt chart figure
        fig = ff.create_gantt(
            gantt_data,
            show_colorbar=True,
            index_col='Task',
            group_tasks=True,
        )
        # Customize figure layout
        # Extract start and finish times for x-axis ticks
        x_ticks = sorted(set(time for task in gantt_data for time in [task['Start'], task['Finish']]))

        # Convert times to strings displaying only seconds
        x_ticks_str = [str(time % 60) for time in x_ticks]

        fig.update_layout(
            xaxis=dict(
                showgrid=True,  # Show grids on the x-axis
                # range=[0, current_time_slot]
                tickvals=x_ticks,
                ticktext=x_ticks_str,
            ),
            yaxis=dict(
                showgrid=True,  # Show grids on the y-axis
            ),
            title_text='Gantt Chart',
            xaxis_title='Time Slots',
            yaxis_title='Tasks',
            xaxis_type='linear',  # Set x-axis type to category
        )
        # Display the Gantt chart using Streamlit
        st.plotly_chart(fig)

def main():
    st.title("Scheduling Algorithms")

    # Liste déroulante en haut de la page
    algo = st.selectbox("Select Scheduling Algorithm",
                        ["RM", "DM","SJF With Preemption", "SJF Without Preemption", "FCFS","EDF"])

    # Afficher la page en fonction de l'algorithme sélectionné
    if algo == "FCFS":
        fcfs_page()
    elif algo == "SJF Without Preemption":
        sjf_page()
    elif algo == "SJF With Preemption":
        sjf_preemption()
    elif algo == "DM":
        DM_page()
    elif algo == "RM":
        RM_page()
    elif algo == "EDF":
        EDF_page()


if __name__ == "__main__":
    main()
