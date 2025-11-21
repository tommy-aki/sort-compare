import random
import time

def heap_sort(arr):
    import heapq
    a = arr.copy()
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]

if __name__ == '__main__':
    size = 50000
    array = [random.randint(1, size * 10) for _ in range(size)]
    for i in range(5):
        start = time.time()
        heap_sort(array)
        timer = time.time() - start

        print(f"{timer}") 