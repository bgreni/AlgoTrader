import time
import sys, os


class Timer:
    """
    Used to timing for testing and performance evaluation purposes
    """
    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.interval = self.end - self.start


class SuppressOut:
    """
    Used to supress unwanted standard output from third party libraries
    """
    def __init__(self):
        self.original_stdout = None
        self.original_stderr = None

    def __enter__(self):
        devnull = open(os.devnull, "w")

        self.original_stdout = sys.stdout
        sys.stdout = devnull

    def __exit__(self, *args, **kwargs):
        sys.stdout = self.original_stdout


def scale_value_distance_from_optimal(actual_value, optimal_value, bound_value):
    """
    Returns a value between 0 and 1
    value will be closer to 0 the further the actual value is from the optimal value,
    becoming 0 when the distance between the actual value and the optimal value exceeds the bound value

    Parameters:
        actual_value (float): The actual value we are evaluating
        optimal_value (float): The optimal value of what actual_value is representing
        bound_value (float): The bound for how much actual_value and optimal_value can differ before the scale value becomes 0

    Returns:
        scale_value (float): value from 0 to 1 evaluating the distance from actual_value to optimal_value
    """
    scale_value = 1 - (abs(actual_value - optimal_value) / bound_value)
    if scale_value < 0:
        return 0
    return scale_value