# SubSet question - Encora - Estagio
from my_set_class import MySet
from auxiliar_function import getSubSets 
import sys

def main():
    """
    Função principal do programa de geração de subconjuntos.
    
    Fluxo do programa:
    1. Solicita ao usuário que digite os elementos do conjunto A (apenas números inteiros).
    2. Permite entrada contínua até que o usuário digite 'fim'.
    3. Valida cada entrada:
       - Se for 'fim': encerra a entrada e prossegue para gerar subconjuntos.
       - Se for número: adiciona ao conjunto A.
       - Se for palavra inválida: encerra o programa com mensagem de erro.
    4. Gera todos os subconjuntos possíveis do conjunto A.
    5. Exibe cada subconjunto e o total de subconjuntos gerados.
    
    Comportamento de erro:
        Se o usuário digitar uma palavra que não é número nem 'fim',
        o programa encerra imediatamente com código de saída 1.
    
    Exemplos:
        Entrada válida: 1, 2, 3, fim
        Saída: todos os subconjuntos de {1, 2, 3}
        
        Entrada inválida: 1, abc
        Saída: mensagem de erro e encerramento do programa
    """

    A = MySet()

    print("Digite os elementos do conjunto A.")
    print("Digite 'fim' para encerrar a entrada.\n")

    while True:
        valor = input("Elemento: ")

        if valor.lower() == "fim":
            break

        # Tenta converter para número se possível
        try:
            valor = int(valor)

        except ValueError:
            # Entrada inválida (não numérica e não 'fim'): encerrar o programa
            print("ERRO")
            print("Entrada inválida: digite somente números ou 'fim' para encerrar.")
            print("Encerrando o programa. Execute novamente para tentar outra vez.")
            sys.exit(1)

        A.add(valor)

    print("\nConjunto A inserido:", A)

    resultado = getSubSets(A)

    print("Subsets encontrados:")
    contador = 0
    for subset in resultado.iterator():
        print(subset)
        contador += 1

    print(f"\nTotal de subsets: {contador}")

if __name__ == "__main__":
    main()