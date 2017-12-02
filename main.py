import Word as wd
import BinaryTree as bt
import AVLTree as avl
import LinkedList as ll
import HashChained as hc
import RedBlackTree as rbt

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


dado1 = wd.Word("Aaorto")
dado2 = wd.Word("Bhiago")
dado3 = wd.Word("Cborta")
dado4 = wd.Word("Deijao")
dado5 = wd.Word("EOiii")
dado6 = wd.Word("FZm")
dado7 = wd.Word("Golo")
dado8 = wd.Word("HAN SOLO!")
dado9 = wd.Word("Izzzzzz")
dado10 = wd.Word("JzzzZZZzzz")


tree = rbt.RedBlackTree()

tree.insert(dado1, compWords)
tree.insert(dado2, compWords)
tree.insert(dado3, compWords)
tree.insert(dado4, compWords)
tree.insert(dado5, compWords)
tree.insert(dado6, compWords)
tree.insert(dado7, compWords)
tree.insert(dado8, compWords)
tree.insert(dado9, compWords)
tree.insert(dado10, compWords)

tree.simmetric()

print(tree.height())


# hash = hc.HashChained(10)
# hash["acc"] = dado1
# hash["add"] = dado2
# hash["app"] = dado3
# hash["aoo"] = dado4
# hash["acc"] = dado8

# print(hash)
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
# root = avl.AVLTree(dado1)

# root = root.insert(dado2, compWords)
# root = root.insert(dado3, compWords)
# root = root.insert(dado4, compWords)
# root = root.insert(dado5, compWords)
# root = root.insert(dado6, compWords)
# root = root.insert(dado7, compWords)
# root = root.insert(dado8, compWords)

# root.simmetric()

# root, data = root.remove("Aborto", compWords)
# root, data = root.remove("Ham", compWords)

# root.simmetric()

