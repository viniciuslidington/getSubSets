#funcoes auxiliares para o código
from my_set_class import MySet

def mask_to_subset(mask, elements):
    """
    Converte uma máscara binária em um subconjunto dos elementos.
    
    Utiliza a representação binária da máscara para determinar quais elementos
    devem fazer parte do subconjunto. Se o bit i está ativado (1), o elemento
    na posição i é incluído no subconjunto.
    
    Args:
        mask (int): Máscara binária que representa o subconjunto (0 a 2^n - 1).
        elements (list): Lista de elementos do conjunto original.
        
    Returns:
        MySet: Um novo conjunto contendo os elementos selecionados pela máscara.
        
    Exemplo:
        Se elements = [1, 2, 3] e mask = 5 (binário: 101),
        retorna um conjunto com {1, 3}.
    """
    subset = MySet()
    n = len(elements)

    for i in range(n):
        if mask & (1 << i):  # se o bit i está ligado
            subset.add(elements[i])

    return subset

def generate_all_subsets(elements):
    """
    Gera todos os subconjuntos possíveis de um conjunto de elementos.
    
    Utiliza o algoritmo de máscara binária para gerar todos os 2^n subconjuntos
    possíveis, incluindo o conjunto vazio e o conjunto completo.
    
    Args:
        elements (list): Lista de elementos do conjunto original.
        
    Returns:
        MySet: Um conjunto contendo todos os subconjuntos possíveis.
               Cada subconjunto é representado como um objeto MySet.
        
    Complexidade:
        O(2^n * n) onde n é o número de elementos.
        
    Exemplo:
        Para elements = [1, 2], retorna:
        {{}, {1}, {2}, {1, 2}}
    """
    result = MySet()
    n = len(elements)
    total_masks = 1 << n  # 2^n

    for mask in range(total_masks):
        subset = mask_to_subset(mask, elements)
        result.add(subset)

    return result


def getSubSets(A):
    """
    Obtém todos os subconjuntos de um conjunto A.
    
    Função principal que converte um conjunto MySet em uma lista de elementos
    e gera todos os seus subconjuntos possíveis.
    
    Args:
        A (MySet): O conjunto do qual se deseja obter todos os subconjuntos.
        
    Returns:
        MySet: Um conjunto contendo todos os subconjuntos possíveis de A.
               Cada subconjunto é um objeto MySet.
        
    Exemplo:
        Se A = {1, 2}, retorna um conjunto com:
        {{}, {1}, {2}, {1, 2}}
    """
    elements = A.toArray()
    return generate_all_subsets(elements)
