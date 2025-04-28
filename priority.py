from typing import List
from ..models.process import Process

def priority_scheduling(processes: List[Process], preemptive: bool = False) -> List[Process]:
    """
    Priority scheduling algorithm (can be preemptive or non-preemptive)
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
            
        # Select process with highest priority (lower number = higher priority)
        next_process = min(arrived, key=lambda x: x.priority)
        
        # Set response time if this is the first time the process gets CPU
        if next_process.response_time == -1:
            next_process.response_time = current_time - next_process.arrival_time
            
        if preemptive:
            # Execute for 1 time unit (preemptive)
            next_process.remaining_time -= 1
            current_time += 1
            
            # Check if process completed
            if next_process.remaining_time == 0:
                next_process.completion_time = current_time
                next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
                next_process.waiting_time = next_process.turnaround_time - next_process.original_burst_time
                completed_processes.append(next_process)
                processes.remove(next_process)
        else:
            # Execute until completion (non-preemptive)
            current_time += next_process.remaining_time
            next_process.remaining_time = 0
            next_process.completion_time = current_time
            next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
            next_process.waiting_time = next_process.turnaround_time - next_process.original_burst_time
            completed_processes.append(next_process)
            processes.remove(next_process)
    
    return completed_processes