import time
from datetime import timedelta

from get_google import get_google

def start_process(max_range=50):
    started_at = time.time()
    for _ in range(max_range):
        get_google()
    elapsed_time = timedelta(seconds=time.time()-started_at)
    return f"Elapsed time without threading {elapsed_time}"