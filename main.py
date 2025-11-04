from pergunta_1 import mover_uns_para_esquerda
from pergunta_2 import buscar_caminho, criar_arvore_exemplo
from pergunta_3 import soma_existe, soma_existe_com_pares
from pergunta_4 import completar_intervalo_com_info


print("=" * 70)
print("  TESTE DE LÓGICA 2025")
print("=" * 70)

print("\nPERGUNTA 1: Array com números '1' à esquerda")
arr1 = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
print(f"Array original: {arr1}")
mover_uns_para_esquerda(arr1)
print(f"Array reordenado: {arr1}")

print("\nPERGUNTA 2: Busca em árvore binária de palavras")
arvore = criar_arvore_exemplo()
palavras = ["Goiaba", "Banana", "Limão", "Cebola"]
for palavra in palavras:
    caminho = buscar_caminho(arvore, palavra)
    if caminho:
        print(f"{palavra}: {' -> '.join(caminho)}")

print("\nPERGUNTA 3: Combinação de soma")
arr3 = [1, 15, 2, 7, 2, 5, 7, 1, 4]
alvos = [9, 16, 3, 100, 8]
for alvo in alvos:
    resultado = soma_existe(arr3, alvo)
    print(f"Soma = {alvo}: {resultado}")

print("\nPERGUNTA 4: Completar intervalo numérico")
arr4 = [9, 2, 3, 1, 4]
info = completar_intervalo_com_info(arr4)
print(f"Array original: {arr4}")
print(f"Maior valor: {info['maior_valor']}")
print(f"Números faltantes: {info['faltantes']}")
print(f"Array completo: {info['array_completo']}")

print("\n" + "=" * 70)
print("  Concluído!")
print("=" * 70)
