#funcoes auxiliares para o código
from my_set_class import MySet

def mask_to_subset(mask, elements):
    subset = MySet()
    n = len(elements)

    for i in range(n):
        if mask & (1 << i):  # se o bit i está ligado
            subset.add(elements[i])

    return subset

def generate_all_subsets(elements):
    result = MySet()
    n = len(elements)
    total_masks = 1 << n  # 2^n

    for mask in range(total_masks):
        subset = mask_to_subset(mask, elements)
        result.add(subset)

    return result


def getSubSets(A):
    elements = A.toArray()
    return generate_all_subsets(elements)
