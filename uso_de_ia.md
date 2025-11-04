# Documentação sobre Uso de Inteligência Artificial

## Contexto

Conforme solicitado no enunciado do teste, este documento descreve como utilizei ferramentas de Inteligência Artificial durante o desenvolvimento das soluções. Acredito que transparência sobre o uso de IA é importante para entender como as soluções foram criadas.

## Ferramentas Utilizadas

**Ferramenta:** Cursor AI e Manus AI

**Período de uso:** 03 e 04 de novembro de 2025 

## Como Usei a IA no Desenvolvimento

### 1. Entendendo os Problemas

Usei a IA principalmente para:
- Entender melhor os requisitos de cada pergunta ao ler o PDF do enunciado
- Clarificar dúvidas sobre o que exatamente cada problema estava pedindo
- Explorar diferentes abordagens possíveis para resolver cada questão

### 2. Desenvolvendo as Soluções

Para cada pergunta, pedi ajuda à IA para:

#### Pergunta 1 - Array com números "1" à esquerda
- Solicitei uma solução simples para reordenar o array movendo os 1s para o início
- A IA sugeriu usar list comprehensions para separar os 1s dos outros números
- Escolhi essa abordagem por ser direta e fácil de entender

#### Pergunta 2 - Busca em árvore binária
- Pedi ajuda para implementar a busca recursiva que retorna o caminho
- A IA me mostrou como construir o caminho durante a recursão
- A estratégia recursiva parecia a mais natural para este problema

#### Pergunta 3 - Combinação de soma
- Solicitei uma solução para verificar se dois números somam um valor alvo
- A IA inicialmente sugeriu usar um conjunto (set) para otimizar
- Preferi uma abordagem mais simples com dois loops, que é mais fácil de entender mesmo sendo menos eficiente

#### Pergunta 4 - Completar intervalo numérico
- Pedi ajuda para identificar números faltantes em um intervalo
- A IA sugeriu usar um conjunto para verificar quais números existem
- Adaptei a solução para usar um loop simples verificando cada número do intervalo

### 3. Organização do Código

A IA me ajudou a:
- Organizar o código em diretórios separados para cada pergunta
- Criar o arquivo `main.py` para executar todas as soluções
- Escrever este README e a documentação sobre uso de IA
- Simplificar o código removendo complexidades desnecessárias

### 4. Testes e Validação

Usei a IA para:
- Verificar se as soluções funcionavam corretamente com os exemplos fornecidos
- Testar se o código executava sem erros
- Garantir que a organização em diretórios não quebrava os imports

## Minhas Decisões

### Por que Python?

Escolhi Python porque:
- É uma linguagem que conheço bem e me sinto confortável
- A sintaxe é clara e facilita a leitura do código
- Não precisa de bibliotecas externas, apenas o que já vem com Python
- É ideal para demonstrar a lógica dos algoritmos de forma clara

## Como Validei as Sugestões

Antes de usar qualquer código sugerido pela IA, sempre:

1. **Testei com os exemplos:** Executei cada solução com os exemplos fornecidos no enunciado para garantir que funcionava corretamente
2. **Executei o código:** Verifiquei que não havia erros de sintaxe ou lógica
3. **Revisei a lógica:** Tentei entender o que o código estava fazendo para ter certeza de que fazia sentido
4. **Simplifiquei quando necessário:** Em alguns casos, preferi soluções mais simples mesmo que não fossem as mais otimizadas

## Meu Processo de Decisão

### Decisões que Tomei

1. **Pergunta 1:** Mantive a solução simples com list comprehensions, mesmo que não seja a mais eficiente em termos de espaço. Preferi clareza sobre otimização.

2. **Pergunta 2:** Escolhi a abordagem recursiva porque achei mais intuitiva e fácil de entender do que uma versão iterativa.

3. **Pergunta 3:** Optei por uma solução com dois loops aninhados (força bruta) ao invés de usar um conjunto. Foi uma escolha consciente de priorizar simplicidade sobre eficiência máxima.

4. **Pergunta 4:** Mantive a solução simples, verificando cada número do intervalo diretamente, sem usar estruturas de dados mais complexas.

## Sobre a Organização dos Commits

Para este teste, optei por fazer um commit único com todas as mudanças ao invés de fazer múltiplos commits menores. Essa escolha foi feita porque:

- O projeto é relativamente pequeno e todas as mudanças estão relacionadas ao mesmo objetivo (completar o teste)
- Facilita a visualização completa do trabalho em um único commit
- Todas as alterações fazem parte do mesmo conjunto de entregas

No entanto, em projetos maiores ou em ambientes de trabalho profissional, minha preferência seria fazer commits menores e mais frequentes.

## Conclusão

A IA foi uma ferramenta útil que me ajudou a:
- Entender melhor os problemas propostos
- Desenvolver as soluções mais rapidamente
- Organizar o código de forma estruturada
- Escrever a documentação

Porém, sempre revisei e testei tudo que a IA sugeriu. Muitas vezes simplifiquei as soluções ou escolhi abordagens diferentes quando achei que faziam mais sentido. O objetivo foi criar soluções que funcionam corretamente e são fáceis de entender, mesmo que não sejam as mais otimizadas possíveis.
