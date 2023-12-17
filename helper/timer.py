import time
from helper import printer


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        printer.info(f"Completed in {elapsed_time:.4f} seconds.")
        return result
    return wrapper
