#!/usr/bin/env python3
""" The basic of async """

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random 'n' times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay value to pass to wait_random.

    Returns:
        List[float]: A list of float values representing the actual delays.

    This function concurrently runs 'n' instances of wait_random with the
    given max_delay. It collects the resulting delays and returns them as
    a list. Each wait_random call waits for a random amount of time between
    0 and max_delay seconds before returning the actual delay.
    """
    batch = []
    for _ in range(n):
        batch.append(await wait_random(max_delay))
    return batch
