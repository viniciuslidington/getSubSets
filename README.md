# getSubSets

Programa em Python para geração de todos os subconjuntos (power set) de um conjunto de números inteiros.

## 📋 Descrição

Este projeto implementa um algoritmo eficiente para gerar todos os subconjuntos possíveis de um conjunto fornecido pelo usuário. Utiliza uma abordagem de máscara binária para garantir que todos os 2^n subconjuntos sejam gerados, incluindo o conjunto vazio e o conjunto completo.

**Desenvolvido para:** Encora - Estágio

## ✨ Funcionalidades

- ✅ Entrada interativa de elementos do conjunto
- ✅ Validação de entrada (apenas números inteiros)
- ✅ Geração automática de todos os subconjuntos
- ✅ Implementação customizada de estrutura de dados Set
- ✅ Algoritmo com complexidade O(2^n * n)
- ✅ Contagem total de subconjuntos gerados

## 🚀 Como Usar

### Pré-requisitos

- Python 3.6 ou superior

### Execução

1. Clone o repositório:
```bash
git clone https://github.com/viniciuslidington/getSubSets.git
cd getSubSets
```

2. Execute o programa:
```bash
python3 main.py
```

3. Siga as instruções na tela:
   - Digite os números inteiros que deseja adicionar ao conjunto
   - Digite `fim` quando terminar de adicionar elementos
   - O programa exibirá todos os subconjuntos gerados

### Exemplo de Uso

```
Digite os elementos do conjunto A.
Digite 'fim' para encerrar a entrada.

Elemento: 1
Elemento: 2
Elemento: 3
Elemento: fim

Conjunto A inserido: {1, 2, 3}
Subsets encontrados:
{}
{1}
{2}
{1, 2}
{3}
{1, 3}
{2, 3}
{1, 2, 3}

Total de subsets: 8
```

## 📁 Estrutura do Projeto

```
getSubSets/
│
├── main.py                 # Arquivo principal com interface do usuário
├── my_set_class.py         # Implementação customizada da classe MySet
├── auxiliar_function.py    # Funções auxiliares para geração de subconjuntos
└── README.md              # Documentação do projeto
```

### Arquivos

#### `main.py`
Contém a função principal do programa que:
- Solicita entrada do usuário
- Valida os dados (apenas números inteiros)
- Coordena a geração de subconjuntos
- Exibe os resultados

#### `my_set_class.py`
Implementação customizada de um conjunto (Set) com os seguintes métodos:
- `add(element)` - Adiciona elemento ao conjunto
- `addAll(other_set)` - Adiciona todos os elementos de outro conjunto
- `contains(element)` - Verifica se elemento existe
- `equals(other_set)` - Compara dois conjuntos
- `iterator()` - Retorna iterador para percorrer elementos
- `remove(element)` - Remove elemento do conjunto
- `size()` - Retorna número de elementos
- `toArray()` - Converte conjunto para lista Python

#### `auxiliar_function.py`
Funções para geração de subconjuntos:
- `mask_to_subset(mask, elements)` - Converte máscara binária em subconjunto
- `generate_all_subsets(elements)` - Gera todos os subconjuntos possíveis
- `getSubSets(A)` - Função principal de geração

## 🔧 Algoritmo

O programa utiliza o **algoritmo de máscara binária** para gerar subconjuntos:

1. Para um conjunto com `n` elementos, existem `2^n` subconjuntos possíveis
2. Cada número de 0 a `2^n - 1` representa um subconjunto único
3. A representação binária do número indica quais elementos incluir:
   - Bit 1 → elemento está no subconjunto
   - Bit 0 → elemento não está no subconjunto

**Exemplo:** Para o conjunto {1, 2, 3}:
- Máscara 5 (binário: 101) → Subconjunto {1, 3}
- Máscara 3 (binário: 011) → Subconjunto {1, 2}

**Complexidade de Tempo:** O(2^n * n)  
**Complexidade de Espaço:** O(2^n)

## ⚠️ Tratamento de Erros

- **Entrada não numérica:** Se o usuário digitar uma palavra que não seja "fim" nem um número, o programa encerra imediatamente com uma mensagem de erro
- **Validação rigorosa:** Apenas números inteiros são aceitos como elementos do conjunto

## 🧪 Testando o Código

Para testar com conjuntos de diferentes tamanhos:

```bash
# Conjunto pequeno (resultado rápido)
python3 main.py
# Digite: 1, 2, fim

# Conjunto médio
python3 main.py
# Digite: 1, 2, 3, 4, fim

# CUIDADO: conjuntos grandes (>20 elementos) podem demorar muito!
```

**Nota:** O número de subconjuntos cresce exponencialmente (2^n), então:
- 3 elementos = 8 subconjuntos
- 10 elementos = 1.024 subconjuntos
- 20 elementos = 1.048.576 subconjuntos

## 📚 Conceitos Utilizados

- **Estruturas de Dados:** Implementação customizada de Set
- **Algoritmos:** Geração de power set com máscaras binárias
- **Programação Orientada a Objetos:** Classes e métodos
- **Manipulação de bits:** Operações bitwise (&, <<)
- **Validação de entrada:** Try-except e tratamento de erros

## 👨‍💻 Autor

Vinicius Lidington

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do processo de estágio na Encora.
