# Teste de Lógica 2025 - Soluções em Python

Este repositório contém minhas soluções para o Teste de Lógica 2025. Desenvolvi as implementações em Python, buscando uma abordagem simples e funcional para cada um dos 4 problemas propostos.

## Estrutura do Projeto

```
teste_logico_2025/
├── README.md           # Este arquivo
├── main.py            # Executa todas as soluções
├── pergunta_1/        # Array com números "1" à esquerda
├── pergunta_2/        # Busca em árvore binária de palavras
├── pergunta_3/        # Combinação de soma
├── pergunta_4/        # Completar intervalo numérico
└── uso_de_ia.md       # Documentação sobre uso de IA
```

Cada diretório `pergunta_X` contém o arquivo `solucao.py` com a implementação da respectiva questão.

## Pré-requisitos

Para executar as soluções, você precisa apenas de:
- **Python 3.7 ou superior** (desenvolvi e testei com Python 3.11)
- Não é necessária nenhuma biblioteca externa, apenas a biblioteca padrão do Python

## Como Executar

### Executar todas as soluções

A forma mais simples é executar o arquivo principal, que roda todas as perguntas em sequência:

```bash
python main.py
```

Ou, se preferir usar Python 3 explicitamente:

```bash
python3 main.py
```

### Executar perguntas individualmente

Se quiser testar apenas uma solução específica, você pode executar diretamente o arquivo de cada pergunta:

```bash
# Pergunta 1
python pergunta_1/solucao.py

# Pergunta 2
python pergunta_2/solucao.py

# Pergunta 3
python pergunta_3/solucao.py

# Pergunta 4
python pergunta_4/solucao.py
```

## Descrição das Soluções

### Pergunta 1: Array com números "1" à esquerda

**O problema:** Preciso reordenar um array de forma que todos os números 1 fiquem no início, mas mantendo a ordem original dos outros elementos.

**Minha abordagem:** Separei os números em dois grupos: primeiro coletei todos os 1s, depois todos os outros elementos. Em seguida, reconstruí o array colocando os 1s primeiro e depois os demais. A função modifica o array original in-place.

**Exemplo:**
```python
Input:  [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
Output: [1, 1, 1, 1, 2, 5, 2, 5, 2, 7, 9, 13, 127, 21]
```

### Pergunta 2: Busca em árvore binária de palavras

**O problema:** Preciso buscar uma palavra em uma árvore binária e retornar o caminho completo que percorri até encontrá-la, no formato "Nó1 -> Nó2 -> Nó3".

**Minha abordagem:** Usei uma busca recursiva em profundidade (DFS). A função verifica se o nó atual é o que procuro. Se não for, busca primeiro na subárvore esquerda e, se não encontrar, busca na direita. Quando encontra, vai construindo o caminho de volta.

**Exemplo:**
```python
Buscar "Goiaba" na árvore
Output: Maçã -> Morango -> Goiaba
```

### Pergunta 3: Combinação de soma

**O problema:** Dado um array e um valor X, preciso verificar se existem dois números no array que, quando somados, resultam em X.

**Minha abordagem:** Usei uma abordagem simples com dois loops aninhados. Para cada número, verifico se existe outro número no array que, somado a ele, dá o valor procurado. É uma solução direta e fácil de entender.

**Exemplo:**
```python
Array: [1, 15, 2, 7, 2, 5, 7, 1, 4]
soma_existe(arr, 9)   -> True  (2 + 7 = 9)
soma_existe(arr, 100) -> False
```

### Pergunta 4: Completar intervalo numérico

**O problema:** Preciso identificar quais números estão faltando no intervalo de 0 até o maior número do array, e então inserir esses números faltantes no próprio array, mantendo tudo ordenado.

**Minha abordagem:** Primeiro encontro o maior valor do array. Depois, percorro de 0 até esse maior valor e verifico quais números não estão no array original. Adiciono esses números faltantes ao array e ordeno tudo no final.

**Exemplo:**
```python
Input:  [9, 2, 3, 1, 4]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Faltantes: [0, 5, 6, 7, 8]
```

## Testes

Cada solução pode ser executada individualmente para testar. Os arquivos incluem exemplos básicos que demonstram o funcionamento das funções.

Quando você executa `main.py`, verá os resultados de todas as perguntas com os exemplos fornecidos no enunciado do teste.

## Como Validar o Resultado

### Executando o Teste Completo

Ao executar `python main.py`, você deve ver uma saída similar a esta:

```
======================================================================
  TESTE DE LÓGICA 2025
======================================================================

PERGUNTA 1: Array com números '1' à esquerda
Array original: [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
Array reordenado: [1, 1, 1, 1, 2, 5, 2, 5, 2, 7, 9, 13, 127, 21]

PERGUNTA 2: Busca em árvore binária de palavras
Goiaba: Maçã -> Morango -> Goiaba
Banana: Maçã -> Pera -> Abacaxi -> Laranja -> Banana
Limão: Maçã -> Morango -> Limão
Cebola: Maçã -> Pera -> Abacaxi -> Laranja -> Cebola

PERGUNTA 3: Combinação de soma
Soma = 9: True
Soma = 16: True
Soma = 3: True
Soma = 100: False
Soma = 8: True

PERGUNTA 4: Completar intervalo numérico
Array original: [9, 2, 3, 1, 4]
Maior valor: 9
Números faltantes: [0, 5, 6, 7, 8]
Array completo: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

======================================================================
  Concluído!
======================================================================
```

### Validação por Pergunta

#### ✅ Pergunta 1 - Validação
**O que verificar:**
- Todos os números `1` devem aparecer no início do array
- Os demais números devem manter a ordem original
- O array deve ter o mesmo tamanho

**Resultado esperado:**
```
Array original: [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
Array reordenado: [1, 1, 1, 1, 2, 5, 2, 5, 2, 7, 9, 13, 127, 21]
```
✅ **Confirmação:** Os 4 números `1` estão no início, seguidos pelos outros números na ordem original.

#### ✅ Pergunta 2 - Validação
**O que verificar:**
- Para cada palavra buscada, deve retornar o caminho completo da raiz até a palavra
- O caminho deve estar no formato "Nó1 -> Nó2 -> Nó3"
- Se a palavra não existir, não deve retornar nada (ou retornar None)

**Resultados esperados:**
- `Goiaba`: `Maçã -> Morango -> Goiaba`
- `Banana`: `Maçã -> Pera -> Abacaxi -> Laranja -> Banana`
- `Limão`: `Maçã -> Morango -> Limão`
- `Cebola`: `Maçã -> Pera -> Abacaxi -> Laranja -> Cebola`

✅ **Confirmação:** Cada caminho mostra o percurso completo da raiz até o nó encontrado.

#### ✅ Pergunta 3 - Validação
**O que verificar:**
- Para cada valor de soma testado, deve retornar `True` se existir um par que some o valor, ou `False` caso contrário
- Os resultados devem ser consistentes com o array fornecido

**Resultados esperados:**
- `Soma = 9: True` (ex: 2 + 7 = 9)
- `Soma = 16: True` (ex: 15 + 1 = 16)
- `Soma = 3: True` (ex: 1 + 2 = 3)
- `Soma = 100: False` (nenhum par soma 100)
- `Soma = 8: True` (ex: 7 + 1 = 8)

✅ **Confirmação:** Os valores `True` indicam que existe pelo menos um par de números que soma o valor alvo.

#### ✅ Pergunta 4 - Validação
**O que verificar:**
- O array deve conter todos os números de 0 até o maior número do array original
- Os números faltantes devem ser identificados corretamente
- O array final deve estar ordenado

**Resultado esperado:**
```
Array original: [9, 2, 3, 1, 4]
Maior valor: 9
Números faltantes: [0, 5, 6, 7, 8]
Array completo: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

✅ **Confirmação:** 
- O maior valor é 9
- Foram identificados 5 números faltantes: 0, 5, 6, 7, 8
- O array final contém todos os números de 0 a 9 em ordem crescente

### Como Confirmar que Está Funcionando Corretamente

1. **Execute o teste completo:**
   ```bash
   python main.py
   ```

2. **Verifique se não há erros:** O programa deve executar sem erros ou exceções.

3. **Compare com os resultados esperados:** Os resultados devem corresponder aos exemplos acima.

4. **Teste individualmente (opcional):** Você pode executar cada pergunta separadamente para validar:
   ```bash
   python pergunta_1/solucao.py
   python pergunta_2/solucao.py
   python pergunta_3/solucao.py
   python pergunta_4/solucao.py
   ```

5. **Validação manual:** Para perguntas 1, 3 e 4, você pode contar manualmente os elementos para confirmar:
   - **Pergunta 1:** Conte quantos `1` existem e verifique se estão no início
   - **Pergunta 3:** Verifique se realmente existe um par que soma cada valor (para os `True`)
   - **Pergunta 4:** Verifique se todos os números de 0 a 9 estão presentes no array final

### Possíveis Problemas

Se você encontrar erros:

- **Erro de importação:** Certifique-se de estar executando a partir da raiz do projeto (onde está o `main.py`)
- **Erro de sintaxe:** Verifique se está usando Python 3.7 ou superior
- **Resultados diferentes:** Verifique se não há modificações no código que alterem a lógica original

## Observações sobre o Código

Tentei manter o código simples e direto ao ponto. As soluções focam em funcionar corretamente e serem fáceis de entender, priorizando clareza sobre otimizações complexas.
