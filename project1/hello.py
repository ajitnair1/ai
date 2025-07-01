name="ajit"
print(f"Hello from {name}")

# Implement a bubble sort function here that sorts integers
# Then call the function passing in a list of 10 randomly generated integers, and print the resulting sorted list
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

random_list = [random.randint(0, 100) for _ in range(10)]
print(f"Original list: {random_list}")
sorted_list = bubble_sort(random_list)
print(f"Sorted list: {sorted_list}")
