import random
import time

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

if __name__ == '__main__':
    size = 50000
    array = [random.randint(1, size * 10) for _ in range(size)]
    for i in range(5):
        start = time.time()
        selection_sort(array)
        timer = time.time() - start

        print(f"Tiempo de ejecución de selection_sort:  {timer}") 