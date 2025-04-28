import time
from typing import List, Dict, Any
from models.process import Process
from utils.process_generator import generate_processes
from utils.metrics import calculate_metrics
from algorithms import (
    fcfs_scheduling,
    sjf_scheduling,
    srtf_scheduling,
    round_robin_scheduling,
    priority_scheduling,
    hrrn_scheduling,
    mlfq_scheduling
)

def reset_processes(processes: List[Process]) -> None:
    """Reset all processes to initial state"""
    for p in processes:
        p.reset()

def run_simulation(processes: List[Process]) -> Dict[str, Dict[str, Any]]:
    """
    Run all scheduling algorithms on the given processes and return metrics
    """
    results = {}
    
    # FCFS
    reset_processes(processes)
    start_time = time.time()
    fcfs_scheduling(processes)
    results['FCFS'] = calculate_metrics(processes)
    results['FCFS']['execution_time'] = time.time() - start_time
    
    # SJF
    reset_processes(processes)
    start_time = time.time()
    sjf_scheduling(processes)
    results['SJF'] = calculate_metrics(processes)
    results['SJF']['execution_time'] = time.time() - start_time
    
    # SRTF
    reset_processes(processes)
    start_time = time.time()
    srtf_scheduling(processes)
    results['SRTF'] = calculate_metrics(processes)
    results['SRTF']['execution_time'] = time.time() - start_time
    
    # Round Robin
    reset_processes(processes)
    start_time = time.time()
    round_robin_scheduling(processes, time_quantum=2)
    results['Round Robin'] = calculate_metrics(processes)
    results['Round Robin']['execution_time'] = time.time() - start_time
    
    # Priority (non-preemptive)
    reset_processes(processes)
    start_time = time.time()
    priority_scheduling(processes, preemptive=False)
    results['Priority NP'] = calculate_metrics(processes)
    results['Priority NP']['execution_time'] = time.time() - start_time
    
    # Priority (preemptive)
    reset_processes(processes)
    start_time = time.time()
    priority_scheduling(processes, preemptive=True)
    results['Priority P'] = calculate_metrics(processes)
    results['Priority P']['execution_time'] = time.time() - start_time
    
    # HRRN
    reset_processes(processes)
    start_time = time.time()
    hrrn_scheduling(processes)
    results['HRRN'] = calculate_metrics(processes)
    results['HRRN']['execution_time'] = time.time() - start_time
    
    # MLFQ
    reset_processes(processes)
    start_time = time.time()
    mlfq_scheduling(processes)
    results['MLFQ'] = calculate_metrics(processes)
    results['MLFQ']['execution_time'] = time.time() - start_time
    
    return results

def print_results(results: Dict[str, Dict[str, Any]]) -> None:
    """Print the simulation results in a formatted table"""
    print("\nCPU Scheduling Algorithm Comparison")
    print("=" * 80)
    print(f"{'Algorithm':<15} {'AWT':<10} {'ATT':<10} {'ART':<10} {'CPU Util':<10} {'Throughput':<10} {'Exec Time':<10}")
    print("-" * 80)
    
    for algo, metrics in results.items():
        print(f"{algo:<15} {metrics['average_waiting_time']:<10.2f} "
              f"{metrics['average_turnaround_time']:<10.2f} "
              f"{metrics['average_response_time']:<10.2f} "
              f"{metrics['cpu_utilization']:<10.2f}% "
              f"{metrics['throughput']:<10.4f} "
              f"{metrics['execution_time']:<10.4f}s")

def main():
    # Generate sample processes
    processes = generate_processes(num_processes=10, max_arrival=20, max_burst=15, max_priority=5)
    
    print("Generated Processes:")
    for p in processes:
        print(p)
    
    # Run simulation
    results = run_simulation(processes)
    
    # Print results
    print_results(results)

if __name__ == "__main__":
    main()