# SubSet question - Encora - Estagio
from mySetClass import MySet

def mask_to_subset(mask, elements):
    subset = MySet()
    n = len(elements)

    for i in range(n):
        if mask & (1 << i):  # se o bit i está ligado
            subset.add(elements[i])

    return subset


# ============================================================
# 3) Função auxiliar: gera todos os subsets possíveis
# ============================================================

def generate_all_subsets(elements):
    result = MySet()
    n = len(elements)
    total_masks = 1 << n  # 2^n

    for mask in range(total_masks):
        subset = mask_to_subset(mask, elements)
        result.add(subset)

    return result


# ============================================================
# 4) Função PRINCIPAL getSubSets(A)
# ============================================================

def getSubSets(A):
    elements = A.toArray()
    return generate_all_subsets(elements)
