#!/usr/bin/env python3
""" this module measure time  """


import time
import typing Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: float, func: Callable) -> float:
    """ Measures the average execution time for a given function """

    start_time = time.time()
    for _ in range(n):
        func(max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
