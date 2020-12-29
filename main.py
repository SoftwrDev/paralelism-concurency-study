import with_threading, without_threading

if __name__ == "__main__":
    result_without = without_threading.start_process(max_range=100)
    result_with = with_threading.start_process(max_range=100)

    print("Results")
    print(result_without)
    print(result_with)