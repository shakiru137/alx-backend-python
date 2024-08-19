#!/usr/bin/env python3
"""The basics of async programming in Python.

This module demonstrates how to use Python's asyncio library to execute
concurrent tasks asynchronously. The primary function, `wait_n`, is designed
to run a specified number of asynchronous tasks concurrently and return the 
results as a list of floats.
"""

import asyncio
from typing import List

# Import the wait_random function from the module '0-basic_async_syntax'
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `wait_random` n times concurrently with the specified `max_delay`.

    This function spawns `n` asynchronous tasks that each call the `wait_random`
    function with a given `max_delay`. It waits for all tasks to complete and 
    returns a list of the actual delays in the order of completion.

    Args:
        n (int): The number of times to spawn the `wait_random` coroutine.
        max_delay (int): The maximum delay value (in seconds) for each `wait_random` call.

    Returns:
        List[float]: A list of floats representing the actual delays experienced 
                     by each call to `wait_random`, ordered by the completion time of the tasks.

    Example:
        >>> asyncio.run(wait_n(5, 10))
        [3.5, 2.7, 5.1, 8.9, 1.4]
    
    Note:
        The order of the returned delays is based on the order of task completion,
        not the order in which the tasks were started.
    """
    # Create a list of asyncio tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Wait for each task to complete and gather the results in the order of completion
    return [await task for task in asyncio.as_completed(tasks)]

