def mover_uns_para_esquerda(arr):
    uns = [x for x in arr if x == 1]
    outros = [x for x in arr if x != 1]
    resultado = uns + outros
    
    for i in range(len(arr)):
        arr[i] = resultado[i]
    
    return arr


if __name__ == "__main__":
    arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
    print("Array original:", arr)
    mover_uns_para_esquerda(arr)
    print("Array reordenado:", arr)

