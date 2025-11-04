class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def buscar_caminho(raiz, palavra):
    if raiz is None:
        return None
    
    if raiz.valor == palavra:
        return [raiz.valor]
    
    caminho = buscar_caminho(raiz.esquerda, palavra)
    if caminho:
        return [raiz.valor] + caminho
    
    caminho = buscar_caminho(raiz.direita, palavra)
    if caminho:
        return [raiz.valor] + caminho
    
    return None


def criar_arvore_exemplo():
    raiz = No("Maçã")
    raiz.esquerda = No("Morango")
    raiz.direita = No("Pera")
    raiz.esquerda.esquerda = No("Goiaba")
    raiz.esquerda.direita = No("Limão")
    raiz.direita.direita = No("Abacaxi")
    raiz.direita.direita.direita = No("Laranja")
    raiz.direita.direita.direita.esquerda = No("Banana")
    raiz.direita.direita.direita.direita = No("Cebola")
    return raiz


if __name__ == "__main__":
    arvore = criar_arvore_exemplo()
    
    palavras = ["Goiaba", "Banana", "Limão", "Cebola"]
    for palavra in palavras:
        caminho = buscar_caminho(arvore, palavra)
        if caminho:
            print(f"{palavra}: {' -> '.join(caminho)}")

