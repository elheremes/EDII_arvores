import sys
import aux
import time
import resource


def main(argv):
    if len(argv) < 2:
        print("Por favor, escolha um TAD.")
    elif len(argv) == 2:
        print("Por favor, selecione pelo menos um documento de texto.")
    else:
        time_start = time.clock()
        words = aux.loadWords(argv[2:])
        if argv[1] == "hash":
            tad = aux.loadHash(words)
            time_elapsed = (time.clock() - time_start)
            print("Tempo para carregar: ", time_elapsed)
            print("Memória usada: ",
                  resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            tad.invertedIndex(words)
        elif argv[1] == "bst":
            tad = aux.loadBinaryTree(words)
            time_elapsed = (time.clock() - time_start)
            print("Tempo para carregar: ", time_elapsed)
            print("Memória usada: ",
                  resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            tad.invertedIndex()
        elif argv[1] == "avl":
            tad = aux.loadAVLTree(words)
            time_elapsed = (time.clock() - time_start)
            print("Tempo para carregar: ", time_elapsed)
            print("Memória usada: ",
                  resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            tad.invertedIndex()
        elif argv[1] == "rb":
            tad = aux.loadRedBlackTree(words)
            time_elapsed = (time.clock() - time_start)
            print("Tempo para carregar: ", time_elapsed)
            print("Memória usada: ",
                  resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            tad.invertedIndex()
        elif argv[1] == "b":
            tad = aux.loadBTree(words)
            time_elapsed = (time.clock() - time_start)
            print("Tempo para carregar: ", time_elapsed)
            print("Memória usada: ",
                  resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            tad.invertedIndex()
        else:
            print("Estrutura TAD escolhida é inválida!")
            sys.exit()

        while True:
            option = int(input("=== Seleciona uma Opção ===\n[1] - IDF\n[2] - Sair\n"))
            
            if option == 2:
                sys.exit()
            elif option == 1:
                time_start = time.clock()
                aux.IDF(argv[2:], tad, argv[1])
                time_elapsed = (time.clock() - time_start)
                print("Tempo para IDF: ", time_elapsed)
                print("Memória usada: ",
                      resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

                
if __name__ == "__main__":
    main(sys.argv)






