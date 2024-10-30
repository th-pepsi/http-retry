import asyncio
import unittest
from retry import is_successful_status, timeOut

loop = asyncio.new_event_loop()

class TestRetryLogic(unittest.TestCase):
    def test_is_successful_status(self):
        self.assertTrue(is_successful_status(200))
        self.assertTrue(is_successful_status(304))
        self.assertFalse(is_successful_status(403))
        self.assertFalse(is_successful_status(502))

    def test_time_out(self):
        res = loop.run_until_complete(timeOut(1))
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
