def completar_intervalo(arr):
    if len(arr) == 0:
        return []
    
    n = max(arr)
    faltantes = []
    
    for i in range(n + 1):
        if i not in arr:
            faltantes.append(i)
    
    arr.extend(faltantes)
    arr.sort()
    
    return arr


def completar_intervalo_com_info(arr):
    if len(arr) == 0:
        return {
            'array_completo': [],
            'faltantes': [],
            'maior_valor': None,
            'quantidade_faltantes': 0
        }
    
    n = max(arr)
    faltantes = []
    
    for i in range(n + 1):
        if i not in arr:
            faltantes.append(i)
    
    arr_copia = arr.copy()
    arr_copia.extend(faltantes)
    arr_copia.sort()
    
    return {
        'array_completo': arr_copia,
        'faltantes': faltantes,
        'maior_valor': n,
        'quantidade_faltantes': len(faltantes)
    }


if __name__ == "__main__":
    arr = [9, 2, 3, 1, 4]
    print(f"Array original: {arr}")
    
    arr_copia = arr.copy()
    completar_intervalo(arr_copia)
    print(f"Array completo: {arr_copia}")

