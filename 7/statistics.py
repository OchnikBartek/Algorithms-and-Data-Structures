from sort import bubble_sort, insertion_sort, quick_sort, heap_sort, merge_sort
import time
import random
import math

def average(times):
    return sum(times) / len(times)

def deviation(times, avg):
    return math.sqrt(sum((x - avg) ** 2 for x in times) / len(times))

def measure_sort_time(sort_function, array, iterations=10):
    times = []
    for _ in range(iterations):
        tablica = array.copy()
        start_time = time.time()
        sort_function(tablica)
        end_time = time.time()
        times.append(end_time - start_time)
    return average(times), deviation(times, average(times))

small_tab = [random.randint(1, 10000) for _ in range(500)]
big_tab = [random.randint(1, 10000) for _ in range(100000)]

with open("Sort_statistics.txt", "w") as fileOutput:
    fileOutput.write(f"NAZWA                -ŚREDNI CZAS-      ODCHYLENIE STANDARDOWE\n"
                     f"--------------------------------------------------------------\n")

    fileOutput.write("dla 500 elementów".center(60) + "\n")
    fileOutput.write("--------------------------------------------------------------\n")

    for name, func in [
        ("1. bąbelkowe", bubble_sort),
        ("2. wstawianie", insertion_sort),
        ("3. szybkie", quick_sort),
        ("4. stogowe", heap_sort),
        ("5. przez scalanie", merge_sort),
    ]:
        avg, dev = measure_sort_time(func, small_tab, iterations=10)
        fileOutput.write(f"{name:20} -- {avg:.5f}s -- {dev:>25.8f}\n")

    fileOutput.write("\n--------------------------------------------------------------\n")
    fileOutput.write("dla 100000 elementów".center(60) + "\n")
    fileOutput.write("--------------------------------------------------------------\n")

    for name, func in [
        ("1. bąbelkowe", bubble_sort),
        ("2. wstawianie", insertion_sort),
        ("3. szybkie", quick_sort),
        ("4. stogowe", heap_sort),
        ("5. przez scalanie", merge_sort),
    ]:
        iterations = 1 if func in [bubble_sort, insertion_sort] else 3
        avg, dev = measure_sort_time(func, big_tab, iterations=iterations)
        fileOutput.write(f"{name:20} -- {avg:.5f}s -- {dev:>25.8f}\n")
