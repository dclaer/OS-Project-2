import random
from typing import List
from ..models.process import Process

def generate_processes(num_processes: int = 5, 
                     max_arrival: int = 10, 
                     max_burst: int = 10, 
                     max_priority: int = 5) -> List[Process]:
    """
    Generate random processes for testing
    """
    processes = []
    for pid in range(1, num_processes + 1):
        arrival_time = random.randint(0, max_arrival)
        burst_time = random.randint(1, max_burst)
        priority = random.randint(1, max_priority)
        processes.append(Process(pid, arrival_time, burst_time, priority))
    return processes