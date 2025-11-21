import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    size = 50000
    array = [random.randint(1, size * 10) for _ in range(size)]
    for i in range(5):
        start = time.time()
        quick_sort(array)
        timer = time.time() - start

        print(f"{timer}") 