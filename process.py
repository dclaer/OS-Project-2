class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.original_burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1  # -1 means not responded yet
        self.completion_time = 0
        
    def __str__(self):
        return (f"Process {self.pid}: Arrival={self.arrival_time}, "
                f"Burst={self.original_burst_time}, Priority={self.priority}")
    
    def reset(self):
        """Reset process to initial state for new simulation"""
        self.remaining_time = self.original_burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1
        self.completion_time = 0