# SubSet question - Encora - Estagio
from my_set_class import MySet
from auxiliar_function import getSubSets 
import sys

def main():

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