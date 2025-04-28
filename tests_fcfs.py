import unittest
from models.process import Process
from algorithms.fcfs import fcfs_scheduling

class TestFCFS(unittest.TestCase):
    def test_fcfs_basic(self):
        processes = [
            Process(1, 0, 5),
            Process(2, 1, 3),
            Process(3, 2, 8)
        ]
        
        scheduled = fcfs_scheduling(processes)
        
        # Check completion times
        self.assertEqual(scheduled[0].completion_time, 5)
        self.assertEqual(scheduled[1].completion_time, 8)
        self.assertEqual(scheduled[2].completion_time, 16)
        
        # Check waiting times
        self.assertEqual(scheduled[0].waiting_time, 0)
        self.assertEqual(scheduled[1].waiting_time, 4)
        self.assertEqual(scheduled[2].waiting_time, 6)
        
    def test_fcfs_with_arrival_gap(self):
        processes = [
            Process(1, 0, 5),
            Process(2, 10, 3),
            Process(3, 12, 8)
        ]
        
        scheduled = fcfs_scheduling(processes)
        
        # Check completion times
        self.assertEqual(scheduled[0].completion_time, 5)
        self.assertEqual(scheduled[1].completion_time, 13)
        self.assertEqual(scheduled[2].completion_time, 21)
        
        # Check waiting times
        self.assertEqual(scheduled[0].waiting_time, 0)
        self.assertEqual(scheduled[1].waiting_time, 0)
        self.assertEqual(scheduled[2].waiting_time, 1)

if __name__ == '__main__':
    unittest.main()