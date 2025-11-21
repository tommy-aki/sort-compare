import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == '__main__':
    size = 50000
    array = [random.randint(1, size * 10) for _ in range(size)]
    for i in range(5):
        start = time.time()
        merge_sort(array)
        timer = time.time() - start

        print(f"{timer}") 