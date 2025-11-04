def soma_existe(arr, alvo):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == alvo:
                return True
    return False


def soma_existe_com_pares(arr, alvo):
    pares = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == alvo:
                pares.append((arr[i], arr[j]))
    return pares


if __name__ == "__main__":
    arr = [1, 15, 2, 7, 2, 5, 7, 1, 4]
    print(f"Array: {arr}")
    
    alvos = [9, 16, 3, 100, 8]
    for alvo in alvos:
        resultado = soma_existe(arr, alvo)
        print(f"Soma = {alvo}: {resultado}")

