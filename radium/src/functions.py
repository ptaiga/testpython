# -*- coding: utf-8 -*-
"""A module containing source code of functions."""

import asyncio
import sys
from hashlib import sha256
from random import SystemRandom


def input_to_sha() -> None:
    """Wait for input data and output sha256 hash from them."""
    sys.stdout.write('\nEnter data:\n')
    text = sys.stdin.readline().rstrip()
    sys.stdout.write(sha256(text.encode('utf-8')).hexdigest())


async def random_print(text: str, max_pause: int = 5) -> None:
    """Print `text` to the console in async-mode with random delay."""
    rnd = SystemRandom()
    pause = rnd.randint(0, max_pause)
    await asyncio.sleep(pause)
    sys.stdout.write(text)


def loop_random_print(messages: list, max_pause: int = 5) -> None:
    """Print a list of text using the asynchronous `random_print` function."""
    loop = asyncio.get_event_loop()
    task_list = [
        loop.create_task(random_print(text, max_pause)) for text in messages
    ]
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()
