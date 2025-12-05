#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ValueError, ZeroDivisionError)
        return None
    finally:
        print("{}".format(result))
    return result
