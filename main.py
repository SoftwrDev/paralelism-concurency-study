import with_threading, without_threading, async_version

def main():
    for max_range in [100, 200, 400, 600]:
        for num_workers in [2, 4, 6]:
            start_process(max_range, num_workers)
            

def start_process(max_range, num_workers):
    result_without = without_threading.start_process(max_range=max_range)
    result_with = with_threading.start_process(workers=num_workers, max_range=max_range)
    result_async = async_version.start_process(max_range=max_range)

    print("Results")
    print(f"{num_workers} workers")
    print(f"Requests number {max_range}")
    print(result_without)
    print(result_with)
    print(result_async + "\n\n")

if __name__ == "__main__":
    main()