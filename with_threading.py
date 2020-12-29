import time
from datetime import timedelta
from concurrent.futures.thread import ThreadPoolExecutor

from get_google import get_google

def start_process(workers=2, max_range=50):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        started_at = time.time()
        for _ in range(max_range):
            executor.submit(get_google)
        elapsed_time = timedelta(seconds=time.time()-started_at)
        return f"Elapsed time with threading {elapsed_time}"