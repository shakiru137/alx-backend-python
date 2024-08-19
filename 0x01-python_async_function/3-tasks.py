#!/usr/bin/env python3
""" The basic of async """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay (in seconds) for the wait_random
        function.

    Returns:
        asyncio.Task: A task object that can be awaited, representing the
        execution of the wait_random coroutine with the specified max_delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
