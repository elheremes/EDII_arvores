import Generic as g
import BinaryTree as bt
import AVLTree as avl

dado1 = g.Generic(1)
dado2 = g.Generic(2)
dado3 = g.Generic(3)
dado4 = g.Generic(10)
dado5 = g.Generic(11)
dado6 = g.Generic(14)
dado7 = g.Generic(14)
dado8 = g.Generic(14)

# root = bt.BinaryTree(dado1)
root = avl.AVLTree(dado1)

root = root.insert(dado2)
root = root.insert(dado3)
root = root.insert(dado4)
root = root.insert(dado5)
root = root.insert(dado6)
root = root.insert(dado7)
root = root.insert(dado8)

root.simmetric()

dado = None
root, dado = root.remove(11, dado)

root.simmetric()
#print(root.balance())

#eoq = root.remove(2)

#print(root.balance(), eoq.getVal())


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
