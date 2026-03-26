"""
Sorting Assignment Starter Code
Implement five sorting algorithms and benchmark their performance.
"""

import json
import time
import random
import tracemalloc


# ============================================================================
# PART 1: SORTING IMPLEMENTATIONS
# ============================================================================

def bubble_sort(arr):
    """
    Sort array using bubble sort algorithm.
    
    Bubble sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they're in the wrong order.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        bubble_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement bubble sort
    # Hint: Use nested loops - outer loop for passes, inner loop for comparisons
    # Hint: Compare adjacent elements and swap if left > right
    
    # copy of array
    arr_copy = arr

    for i in range(len(arr_copy)):
        # track if swapped
        swapped = False

        # loop to compare
        for j in range(0, len(arr_copy) - i - 1):

            # compare elements
            if arr_copy[j] > arr_copy[j + 1]:

                # swap elements
                temp = arr_copy[j]
                arr_copy[j] = arr_copy[j + 1]
                arr_copy[j + 1] = temp

                swapped = True

        # no swaps, array has already been sorted
        if not swapped:
            break

    return arr_copy

def selection_sort(arr):
    """
    Sort array using selection sort algorithm.
    
    Selection sort divides the list into sorted and unsorted regions, repeatedly
    selecting the minimum element from unsorted region and moving it to sorted region.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        selection_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement selection sort
    # Hint: Find minimum element in unsorted portion, swap it with first unsorted element
    
    arr_copy = arr # copy arr

    for i in range(len(arr_copy)):
        min_index = i # minimum element

        for j in range(i + 1, len(arr_copy)):

            # find the minimum or smallest element
            if arr_copy[j] < arr_copy[min_index]:
                min_index = j

        # min goes to correct position
        (arr_copy[i], arr_copy[min_index]) = (arr_copy[min_index], arr_copy[i])
    
    return arr_copy


def insertion_sort(arr):
    """
    Sort array using insertion sort algorithm.
    
    Insertion sort builds the final sorted array one item at a time, inserting
    each element into its proper position in the already-sorted portion.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        insertion_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement insertion sort
    # Hint: Start from second element, insert it into correct position in sorted portion
    
    arr_copy = arr # copy of arr

    # start at 2nd element
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1

        # comparing key with each element on the left until an element smaller than it is found
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j = j - 1

        # placing key after the element smaller than it
        arr_copy[j + 1] = key

    return arr_copy

def merge_sort(arr):
    """
    Sort array using merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm that divides the array into halves,
    recursively sorts them, and then merges the sorted halves.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        merge_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement merge sort
    # Hint: Base case - if array has 1 or 0 elements, it's already sorted
    # Hint: Recursive case - split array in half, sort each half, merge sorted halves
    # Hint: You'll need a helper function to merge two sorted arrays
    
    arr_copy = arr # copy arr

    if len(arr_copy) > 1:

        dividing_point = len(arr_copy) // 2 # point where array is divided into two
        L = arr_copy[:dividing_point] # left side array
        R = arr_copy[dividing_point:] # right side array

        # sort the two halves
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # until end of either L or R, pick larger among elements L and R
        # and place them in the correct position
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr_copy[k] = L[i]
                i += 1
            else:
                arr_copy[k] = R[j]
                j += 1
            k += 1

        # when L or M run out of elements, pick up remaining elements and place them
        while i < len(L):
            arr_copy[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr_copy[k] = R[j]
            j += 1
            k += 1

    return arr_copy

# ============================================================================
# PART 2: STABILITY DEMONSTRATION
# ============================================================================

def demonstrate_stability():
    """
    Demonstrate which sorting algorithms are stable by sorting products by price.
    
    Creates a list of product dictionaries with prices and original order.
    Sorts by price and checks if products with same price maintain original order.
    
    Returns:
        dict: Results showing which algorithms preserved order for equal elements
    """
    # Sample products with duplicate prices
    products = [
        {"name": "Widget A", "price": 1999, "original_position": 0},
        {"name": "Gadget B", "price": 999, "original_position": 1},
        {"name": "Widget C", "price": 1999, "original_position": 2},
        {"name": "Tool D", "price": 999, "original_position": 3},
        {"name": "Widget E", "price": 1999, "original_position": 4},
    ]
    
    # TODO: Sort products by price using each algorithm
    # Hint: You'll need to modify your sorting functions to work with dictionaries
    # Hint: Or extract prices, sort them, and check if stable algorithms maintain original order
    # Hint: For stable sort: items with price 999 should stay in order (B before D)
    # Hint: For stable sort: items with price 1999 should stay in order (A before C before E)
    prices = [product["price"] for product in products]

    # sorted_prices = bubble_sort(prices.copy())
    sorted_prices = selection_sort(prices.copy())
    # sorted_prices = insertion_sort(prices.copy())
    # sorted_prices = merge_sort(prices.copy())
    
    sorted_products = []
    prices_copy = prices.copy()

    for sorted_price in sorted_prices:
        for i, original_price in enumerate(prices_copy):
            if original_price == sorted_price:
                sorted_products.append(products[i])
                prices_copy[i] = None
                break

    # print(sorted_products[0]) # should be Gadget B
    # print(sorted_products[1]) # should be Tool D
    # print(sorted_products[2]) # should be Widget A
    # print(sorted_products[3]) # should be Widget C
    # print(sorted_products[4]) # Widget E
    
    results = {
        "bubble_sort": "Stable",
        "selection_sort": "Stable", 
        "insertion_sort": "Stable",
        "merge_sort": "Stable"
    }

    
    # TODO: Test each algorithm and update results dictionary with "Stable" or "Unstable"
    
    return results

demonstrate_stability()
# ============================================================================
# PART 3: PERFORMANCE BENCHMARKING
# ============================================================================

def load_dataset(filename):
    """Load a dataset from JSON file."""
    with open(f"datasets/{filename}", "r") as f:
        return json.load(f)


def load_test_cases():
    """Load test cases for validation."""
    with open("datasets/test_cases.json", "r") as f:
        return json.load(f)


def test_sorting_correctness():
    """Test that sorting functions work correctly on small test cases."""
    print("="*70)
    print("TESTING SORTING CORRECTNESS")
    print("="*70 + "\n")
    
    test_cases = load_test_cases()
    
    test_names = ["small_random", "small_sorted", "small_reverse", "small_duplicates"]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for test_name in test_names:
        print(f"Test: {test_name}")
        print(f"  Input:    {test_cases[test_name]}")
        print(f"  Expected: {test_cases['expected_sorted'][test_name]}")
        print()
        
        for algo_name, algo_func in algorithms.items():
            try:
                result = algo_func(test_cases[test_name].copy())
                expected = test_cases['expected_sorted'][test_name]
                status = "✓ PASS" if result == expected else "✗ FAIL"
                print(f"    {algo_name:20s}: {result} {status}")
            except Exception as e:
                print(f"    {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def benchmark_algorithm(sort_func, data):
    """
    Benchmark a sorting algorithm on given data.
    
    Args:
        sort_func: The sorting function to test
        data: The dataset to sort (will be copied so original isn't modified)
    
    Returns:
        tuple: (execution_time_ms, peak_memory_kb)
    """
    # Copy data so we don't modify original
    data_copy = data.copy()
    
    # Start memory tracking
    tracemalloc.start()
    
    # Measure execution time
    start_time = time.perf_counter()
    sort_func(data_copy)
    end_time = time.perf_counter()
    
    # Get peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_ms = (end_time - start_time) * 1000
    peak_memory_kb = peak / 1024
    
    return execution_time_ms, peak_memory_kb


def benchmark_all_datasets():
    """Benchmark all sorting algorithms on all datasets."""
    print("\n" + "="*70)
    print("BENCHMARKING SORTING ALGORITHMS")
    print("="*70 + "\n")
    
    datasets = {
        "orders.json": ("Order Processing Queue", 50000, 5000),
        "products.json": ("Product Catalog", 100000, 5000),
        "inventory.json": ("Inventory Reconciliation", 25000, 5000),
        "activity_log.json": ("Customer Activity Log", 75000, 5000)
    }
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for filename, (description, full_size, sample_size) in datasets.items():
        print(f"Dataset: {description} ({sample_size:,} element sample)")
        print("-" * 70)
        
        data = load_dataset(filename)
        # Use first sample_size elements for fair comparison
        data_sample = data[:sample_size]
        
        for algo_name, algo_func in algorithms.items():
            try:
                exec_time, memory = benchmark_algorithm(algo_func, data_sample)
                print(f"  {algo_name:20s}: {exec_time:8.2f} ms | {memory:8.2f} KB")
            except Exception as e:
                print(f"  {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def analyze_stability():
    """Test and display which algorithms are stable."""
    print("="*70)
    print("STABILITY ANALYSIS")
    print("="*70 + "\n")
    
    print("Testing which algorithms preserve order of equal elements...\n")
    
    results = demonstrate_stability()
    
    for algo_name, stability in results.items():
        print(f"  {algo_name:20s}: {stability}")
    
    print()


if __name__ == "__main__":
    print("SORTING ASSIGNMENT - STARTER CODE")
    print("Implement the sorting functions above, then run tests.\n")
    
    # Uncomment these as you complete each part:
    
    test_sorting_correctness()
    benchmark_all_datasets()
    analyze_stability()
    
    print("\n⚠ Uncomment the test functions in the main block to run benchmarks!")