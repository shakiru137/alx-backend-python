#!/usr/bin/env python3
""" Basic of async """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `task_wait_random` n times concurrently with the specified `max_delay`

    This function spawns `n` asynchronous tasks, each calling the
    `task_wait_random`
    function with the given `max_delay`. It waits for all tasks to complete and
    returns a list of the actual delays in the order of their completion.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay (in seconds) for each task.

    Returns:
        List[float]: A list of floats representing the actual delay
        experienced by each task, ordered by the completion time of the tasks.
    """
    # Create a list of asyncio tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Wait for each task to complete and gather the results in the order
    # of completion
    return [await task for task in asyncio.as_completed(tasks)]
