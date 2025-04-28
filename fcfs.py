from typing import List
from ..models.process import Process

def fcfs_scheduling(processes: List[Process]) -> List[Process]:
    """
    First Come First Serve scheduling algorithm
    """
    # Sort processes by arrival time
    ready_queue = sorted(processes, key=lambda x: x.arrival_time)
    
    current_time = 0
    for process in ready_queue:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
            
        # Set response time (first time process gets CPU)
        if process.response_time == -1:
            process.response_time = current_time - process.arrival_time
            
        # Execute the process
        current_time += process.remaining_time
        process.remaining_time = 0
        process.completion_time = current_time
        
        # Calculate turnaround time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.original_burst_time
    
    return ready_queue