#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
