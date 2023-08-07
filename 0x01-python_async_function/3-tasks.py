#!/usr/bin/env python3
""" this module creates a regular function named task_wait_random"""


import asyncio
from typing import Task
from random_delay import wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Creates and returns an asyncio.Task for wait_random"""

    return asyncio.create_task(wait_random(max_delay))
