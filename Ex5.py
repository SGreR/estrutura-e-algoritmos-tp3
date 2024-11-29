def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivot]
    meio = [x for x in arr if x == pivot]
    direita = [x for x in arr if x > pivot]
    return quicksort(esquerda) + meio + quicksort(direita)