from typing import List
from ..models.process import Process

def calculate_metrics(processes: List[Process]) -> dict:
    """
    Calculate performance metrics for a list of processes
    """
    if not processes:
        return {}
    
    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    total_response_time = sum(p.response_time for p in processes)
    total_burst_time = sum(p.original_burst_time for p in processes)
    total_completion_time = max(p.completion_time for p in processes) if processes else 0
    
    num_processes = len(processes)
    
    metrics = {
        'average_waiting_time': total_waiting_time / num_processes,
        'average_turnaround_time': total_turnaround_time / num_processes,
        'average_response_time': total_response_time / num_processes,
        'cpu_utilization': (total_burst_time / total_completion_time) * 100 if total_completion_time > 0 else 0,
        'throughput': num_processes / total_completion_time if total_completion_time > 0 else 0
    }
    
    return metrics