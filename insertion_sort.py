import random
import time

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

if __name__ == '__main__':
    size = 50000
    array = [random.randint(1, size * 10) for _ in range(size)]

    start = time.time()
    insertion_sort(array)
    timer = time.time() - start

    print(f"Tiempo de ejecución de insertion_sort:  {timer}") 

