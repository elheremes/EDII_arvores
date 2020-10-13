import sys

class Tree_Node(object):
    def __init__(self, word):
        self.palavra = word
        self.occ= 1
        self.left = None
        self.right = None
        self.height = 1

#NÓ DA ARVORE
class AVL_Tree(object):
    def insert(self, root, key):

        if self.search(root,key) == 0:
            root.occ+=1
            return root

        if not root:
            return Tree_Node(key)
        elif key< root.palavra:
            root.left=self.insert(root.left, key)
        else:
            root.right=self.insert(root.right, key)
    
        root.height= 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance= self.getBalance(root)

        if balance > 1 and key < root.left.palavra:
            return self.rightRotate(root)

        if balance < -1 and key> root.right.palavra:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.palavra:
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and key < root.right.palavra:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    def leftRotate (self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate (self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def getHeight(self, root):
        if not root:
            return 0
        
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0}  {1} -- ".format(root.palavra,root.occ), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

    def search(self,root, val):
        if root:
            if root.palavra == val:
                return 0
            elif val<root.palavra:
                self.search(root.left, val)
            else:
                self.search(root.right, val)
                
    
        return -1