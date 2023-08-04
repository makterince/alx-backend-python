#!/usr/bin/env python3
""" module corrects a function """


from typing import Dict, TypeVar


KT = TypeVar('KT')
VT = TypeVar('VT')


def safely_get_value(dct: Dict[KT, VT], key: KT, default: VT = None) -> VT:
    """ Get a value from a dictionary safely."""

    if key in dct:
        return dct[key]
    else:
        return default
