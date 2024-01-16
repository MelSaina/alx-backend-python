#!/usr/bin/env python3

''' Task 02'''

import asyncio
from time import time
from importlib import import_module as using

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    Executes async_comprehension 4 times and measures the
    total execution time.
    '''

    start_time = time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time()
    return end_time - start_time

