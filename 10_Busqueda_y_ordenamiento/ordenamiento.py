import random
import timeit

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >=0 and key < arr[j] :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

def generate_random_list(size):
  return [random.randint(1, 1000) for _ in range(size)]

# Lista aleatoria
random_list = generate_random_list(10000)

# Lista no aleatoria
lista = [5,4,23,2,1,45,212,32,54]

# Medir tiempo para la lista ordenada
start_time = timeit.default_timer()
insertion_sort(lista.copy())
end_time = timeit.default_timer()
print("Tiempo para lista pequeña:", end_time - start_time)

# Medir tiempo para la lista aleatoria
start_time = timeit.default_timer()
insertion_sort(random_list.copy())
end_time = timeit.default_timer()
print("Tiempo para lista grande:", end_time - start_time)