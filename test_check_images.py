import unittest
from check_images import main

class TestTimingCode(unittest.TestCase):
    def test_timing_format(self):
        from time import time
        start_time = time()
        end_time = start_time + 3661 

        tot_time = end_time - start_time

        hours = int(tot_time / 3600)
        minutes = int((tot_time % 3600) / 60)
        seconds = int(tot_time % 60)

        self.assertEqual(hours, 1)
        self.assertEqual(minutes, 1)
        self.assertEqual(seconds, 1)

if __name__ == "__main__":
    unittest.main()
