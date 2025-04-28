from typing import List
from collections import deque
from ..models.process import Process

def round_robin_scheduling(processes: List[Process], time_quantum: int = 2) -> List[Process]:
    """
    Round Robin scheduling algorithm
    """
    processes = [p for p in processes]  # Create a copy
    ready_queue = deque()
    current_time = 0
    completed_processes = []
    
    # Sort by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    
    while processes or ready_queue:
        # Add arrived processes to ready queue
        while processes and processes[0].arrival_time <= current_time:
            ready_queue.append(processes.pop(0))
            
        if not ready_queue:
            current_time += 1
            continue
            
        current_process = ready_queue.popleft()
        
        # Set response time if this is the first time the process gets CPU
        if current_process.response_time == -1:
            current_process.response_time = current_time - current_process.arrival_time
            
        # Execute for time quantum or until process completes
        execution_time = min(time_quantum, current_process.remaining_time)
        current_process.remaining_time -= execution_time
        current_time += execution_time
        
        # Check if process completed
        if current_process.remaining_time == 0:
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.original_burst_time
            completed_processes.append(current_process)
        else:
            # Add back to ready queue if not completed
            ready_queue.append(current_process)
    
    return completed_processes