# import Generic as g
import Word as wd
# import BinaryTree as bt
import AVLTree as avl
# import LinkedList as ll
# import HashChained as hc


C = 8


def comp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0


def compWords(x, y):
    global C
    if x[0:C] > y[0:C]:
        return 1
    elif x[0:C] < y[0:C]:
        return -1
    return 0


dado1 = wd.Word("Aborto")
dado2 = wd.Word("Thiago")
dado3 = wd.Word("Aborta")
dado4 = wd.Word("Feijao")
dado5 = wd.Word("Oiii")
dado6 = wd.Word("Ham")
dado7 = wd.Word("Solo")
dado8 = wd.Word("HAN SOLO!")

# list = ll.LinkedList()

# list.insert(dado1)
# list.insert(dado5)
# list.insert(dado7)
# list.insert(dado2)
# print(list, list.length())

# aux = list.search(14)
# print(list, list.length())
# print(aux.getVal())

# root = bt.BinaryTree(dado1)
root = avl.AVLTree(dado1)

root = root.insert(dado2, compWords)
root = root.insert(dado3, compWords)
root = root.insert(dado4, compWords)
root = root.insert(dado5, compWords)
root = root.insert(dado6, compWords)
root = root.insert(dado7, compWords)
root = root.insert(dado8, compWords)

root.simmetric()

root, data = root.remove("Aborto", compWords)
root, data = root.remove("Ham", compWords)

root.simmetric()

