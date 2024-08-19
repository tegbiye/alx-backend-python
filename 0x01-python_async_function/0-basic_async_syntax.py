#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
  """
  Waits for a random delay between 0 and max_delay seconds and returns the delay.

  Args:
    max_delay: The maximum delay in seconds. Defaults to 10.

  Returns:
    The actual delay in seconds.
  """

  delay = random.uniform(0, max_delay)
  await asyncio.sleep(delay)
  return delay
