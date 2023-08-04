#!/usr/bin/env python3
"""
modules correct a function given
"""


from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """ Get the first element of a list safely. """

    if lst:
        return lst[0]
    else:
        return None
