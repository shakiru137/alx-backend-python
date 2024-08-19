#!/usr/bin/env python3
""" The basic of asycn """

import asyncio
import time

# Import the wait_n function from the module '1-concurrent_coroutines'
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken by the wait_n function to execute.

    Args:
        n (int): The number of concurrent tasks to run.
        max_delay (int): The maximum delay value for each task.

    Returns:
        float: The average time taken per task.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    # Calculate total elapsed time and average time per task
    total_time = end_time - start_time
    return total_time / n
