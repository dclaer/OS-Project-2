from typing import List
from collections import deque
from ..models.process import Process

def mlfq_scheduling(processes: List[Process], 
                   num_queues: int = 3,
                   time_quantums: List[int] = [5, 10, -1],
                   boost_time: int = 100) -> List[Process]:
    """
    Multi-Level Feedback Queue scheduling algorithm
    
    Parameters:
    - num_queues: Number of priority queues (default 3)
    - time_quantums: Time quantum for each queue (last queue is FCFS if -1)
    - boost_time: Time interval for priority boost (move all processes to top queue)
    """
    if len(time_quantums) != num_queues:
        raise ValueError("Number of time quantums must match number of queues")
    
    processes = [p for p in processes]  # Create a copy
    queues = [deque() for _ in range(num_queues)]
    current_time = 0
    completed_processes = []
    last_boost_time = 0
    
    # Initialize all processes in the top priority queue (queue 0)
    processes.sort(key=lambda x: x.arrival_time)
    
    while processes or any(queues):
        # Priority boost if boost_time has passed
        if current_time - last_boost_time >= boost_time and boost_time > 0:
            for q in queues[1:]:
                while q:
                    queues[0].append(q.popleft())
            last_boost_time = current_time
            
        # Add arrived processes to top priority queue
        while processes and processes[0].arrival_time <= current_time:
            queues[0].append(processes.pop(0))
            
        # Find the highest priority non-empty queue
        current_queue = next((i for i, q in enumerate(queues) if q), None)
        
        if current_queue is None:
            current_time += 1
            continue
            
        current_process = queues[current_queue].popleft()
        
        # Set response time if this is the first time the process gets CPU
        if current_process.response_time == -1:
            current_process.response_time = current_time - current_process.arrival_time
            
        # Determine time quantum for current queue
        quantum = time_quantums[current_queue]
        if quantum == -1:  # FCFS for lowest queue
            execution_time = current_process.remaining_time
        else:
            execution_time = min(quantum, current_process.remaining_time)
            
        # Execute the process
        current_process.remaining_time -= execution_time
        current_time += execution_time
        
        # Check if process completed
        if current_process.remaining_time == 0:
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.original_burst_time
            completed_processes.append(current_process)
        else:
            # Demote to lower priority queue if not completed
            next_queue = min(current_queue + 1, num_queues - 1)
            queues[next_queue].append(current_process)
    
    return completed_processes