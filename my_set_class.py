#classe Set crua
class MySet:
    """
    Implementação customizada de um conjunto (Set) sem repetições.
    
    Utiliza uma lista interna para armazenar elementos únicos, fornecendo
    operações básicas de conjunto como adicionar, remover e verificar elementos.
    """
    
    def __init__(self):
        """
        Inicializa um conjunto vazio.
        """
        self.data = []  # lista interna para armazenar elementos sem repetição

    def add(self, element):
        """
        Adiciona um elemento ao conjunto se ele ainda não existir.
        
        Args:
            element: O elemento a ser adicionado ao conjunto.
            
        Returns:
            bool: True se o elemento foi adicionado, False se já existia.
        """
        if element not in self.data:
            self.data.append(element)
            return True
        return False

    def addAll(self, other_set):
        """
        Adiciona todos os elementos de outro conjunto a este conjunto.
        
        Args:
            other_set (MySet): O conjunto cujos elementos serão adicionados.
            
        Returns:
            bool: True se pelo menos um elemento foi adicionado, False caso contrário.
        """
        changed = False
        for element in other_set.data:
            if self.add(element):
                changed = True
        return changed

    def contains(self, element):
        """
        Verifica se um elemento está presente no conjunto.
        
        Args:
            element: O elemento a ser verificado.
            
        Returns:
            bool: True se o elemento está no conjunto, False caso contrário.
        """
        return element in self.data

    def equals(self, other_set):
        """
        Verifica se este conjunto é igual a outro conjunto.
        
        Dois conjuntos são considerados iguais se possuem o mesmo tamanho
        e contêm exatamente os mesmos elementos.
        
        Args:
            other_set (MySet): O conjunto a ser comparado.
            
        Returns:
            bool: True se os conjuntos são iguais, False caso contrário.
        """
        if self.size() != other_set.size():
            return False
        for e in self.data:
            if not other_set.contains(e):
                return False
        return True

    def iterator(self):
        """
        Retorna um iterador para percorrer os elementos do conjunto.
        
        Returns:
            iterator: Um iterador sobre os elementos do conjunto.
        """
        return iter(self.data)

    def remove(self, element):
        """
        Remove um elemento do conjunto se ele existir.
        
        Args:
            element: O elemento a ser removido.
            
        Returns:
            bool: True se o elemento foi removido, False se não existia.
        """
        if element in self.data:
            self.data.remove(element)
            return True
        return False

    def size(self):
        """
        Retorna o número de elementos no conjunto.
        
        Returns:
            int: O tamanho do conjunto.
        """
        return len(self.data)

    def toArray(self):
        """
        Converte o conjunto para uma lista Python.
        
        Returns:
            list: Uma cópia dos elementos do conjunto como lista.
        """
        return list(self.data)

    def __repr__(self):
        """
        Retorna uma representação em string do conjunto.
        
        Returns:
            str: O conjunto formatado como "{elemento1, elemento2, ...}".
        """
        if self.size() == 0:
            return "{}"
        return "{" + ", ".join(str(e) for e in self.data) + "}"