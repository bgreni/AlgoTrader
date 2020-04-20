import time
import sys, os


class Timer:    
    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.interval = self.end - self.start


class SuppressOut:
    def __init__(self):
        self.original_stdout = None
        self.original_stderr = None

    def __enter__(self):
        devnull = open(os.devnull, "w")

        self.original_stdout = sys.stdout
        sys.stdout = devnull

    def __exit__(self, *args, **kwargs):
        sys.stdout = self.original_stdout