#!/usr/bin/env python3
""" this module measure time  """


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the average execution time for a given function """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    average_time = total_time / n
    return average_time
