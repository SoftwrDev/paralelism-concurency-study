import with_threading, without_threading, async_version

if __name__ == "__main__":
    result_without = without_threading.start_process(max_range=100)
    result_with = with_threading.start_process(max_range=100)
    result_async = async_version.start_process(max_range=100)

    print("Results")
    print(result_without)
    print(result_with)
    print(result_async)