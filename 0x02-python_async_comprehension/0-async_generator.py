#!/usr/bin/env python3
""" Async Comprehension """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates a sequence of 10 random float numbers between
    0 and 10.

    This coroutine will:
    1. Loop 10 times.
    2. In each iteration, it will:
        a. Pause for 1 second using asyncio.sleep().
        b. Yield a random floating-point number between 0 and 10.

    Yields:
        float: A random float number between 0 and 10.

    Example usage:
        >>> async def main():
        >>>     async for value in async_generator():
        >>>         print(value)
        >>> asyncio.run(main())
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
