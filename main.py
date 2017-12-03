import sys
import aux

def main(argv):
    if len(argv) < 2:
        print("Por favor, escolha um TAD.")
    elif len(argv) == 2:
        print("Por favor, selecione pelo menos um documento de texto.")
    else:
        words = aux.loadWords(argv[2:])
        if argv[1] == "hash":
            tad = aux.loadHash(words)
            tad.invertedIndex(words)
        elif argv[1] == "bst":
            tad = aux.loadBinaryTree(words)
            tad.invertedIndex()
        elif argv[1] == "avl":
            tad = aux.loadAVLTree(words)
            tad.invertedIndex()
        elif argv[1] == "rb":
            tad = aux.loadRedBlackTree(words)
            tad.invertedIndex()
        else:
            print("Estrutura TAD escolhida é inválida!")
            sys.exit()

        while True:
            option = int(input("=== Seleciona uma Opção ===\n[1] - IDF\n[2] - Sair\n"))
            
            if option == 2:
                sys.exit()
            elif option == 1:
                aux.IDF(argv[2:], tad, argv[1])

                
if __name__ == "__main__":
    main(sys.argv)






