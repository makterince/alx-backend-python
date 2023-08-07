#!/usr/bin/env python3
""" this module waits a random delay and returns its argument """


import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
        Waits for a random delay between 0 and max_delay seconds
        Args:
            max_delay (float): The maximum delay in seconds. Default is 10.

        Returns:
            float: The random delay that was waited for.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    asyncio.run(wait_random())
