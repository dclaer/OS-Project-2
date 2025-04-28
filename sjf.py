from typing import List
from ..models.process import Process

def sjf_scheduling(processes: List[Process]) -> List[Process]:
    """
    Shortest Job First (non-preemptive) scheduling algorithm
    """
    processes = [p for p in processes]  # Create a copy
    current_time = 0
    completed_processes = []
    
    while processes:
        # Get arrived processes
        arrived = [p for p in processes if p.arrival_time <= current_time]
        
        if not arrived:
            current_time += 1
            continue
            
        # Select process with shortest burst time
        next_process = min(arrived, key=lambda x: x.remaining_time)
        
        # Set response time
        if next_process.response_time == -1:
            next_process.response_time = current_time - next_process.arrival_time
            
        # Execute the process
        current_time += next_process.remaining_time
        next_process.remaining_time = 0
        next_process.completion_time = current_time
        
        # Calculate turnaround and waiting time
        next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
        next_process.waiting_time = next_process.turnaround_time - next_process.original_burst_time
        
        # Move to completed
        completed_processes.append(next_process)
        processes.remove(next_process)
    
    return completed_processes