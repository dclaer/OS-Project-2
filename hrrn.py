from typing import List
from ..models.process import Process

def hrrn_scheduling(processes: List[Process]) -> List[Process]:
    """
    Highest Response Ratio Next scheduling algorithm
    """
    processes = [p for p in processes]  # Create a copy
    current_time = 0
    completed_processes = []
    
    while processes:
        # Get arrived processes with remaining time > 0
        arrived = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
        
        if not arrived:
            current_time += 1
            continue
            
        # Calculate response ratio for each process
        for p in arrived:
            waiting_time = current_time - p.arrival_time
            p.response_ratio = (waiting_time + p.original_burst_time) / p.original_burst_time
            
        # Select process with highest response ratio
        next_process = max(arrived, key=lambda x: x.response_ratio)
        
        # Set response time if this is the first time the process gets CPU
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