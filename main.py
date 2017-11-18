import Generic as g
# import BinaryTree as bt
# import AVLTree as avl
# import LinkedList as ll
import HashChained as hc

dado1 = g.Generic(1)
dado2 = g.Generic(2)
dado3 = g.Generic(3)
dado4 = g.Generic(10)
dado5 = g.Generic(11)
dado6 = g.Generic(14)
dado7 = g.Generic(14)
dado8 = g.Generic(14)


hash = hc.HashChained(5)

hash["batata"] = dado1
hash["feijao"] = dado2
hash["sol"] = dado3
print(hash)



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

# root = root.insert(dado2)
# root = root.insert(dado3)
# root = root.insert(dado4)
# root = root.insert(dado5)
# root = root.insert(dado6)
# root = root.insert(dado7)
# root = root.insert(dado8)

# root.simmetric()
# print("\n\n\n")

# eoq = root.remove(8)

# print(eoq.getVal(), "\n\n\n")

# root.simmetric()
# print("\n\n\n")

# eoq = root.remove(3)
# root.simmetric()

# print(root.height())

# print(root.maxTree())

# print(root.minTree())
