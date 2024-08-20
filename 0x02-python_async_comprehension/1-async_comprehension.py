#!/usr/bin/env python3
""" Async comprehension """

import asyncio
from typing import List

# Import async_generator from the module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    # Collecting 10 random numbers using async comprehension
    result = [i async for i in async_generator()]
    return result
