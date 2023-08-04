#!/usr/bin/env python3
""" module corrects a function """


from typing import Tuple, List, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """ Zooms in on elements of a tuple by repeating them a
        specified number of times
    """

    zoomed_in: List[int] = [
            item for item in lst
            for i in range(factor)
    ]
    return zoomed_in

array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
