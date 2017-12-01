class RedBlackNode:
    def __init__(self, data=None, left=None, right=None, parent=None,
                 color=True):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

    def __str__(self):
        return (str(self.__data.getVal())) + "\n"

    
class RedBlackTree:
    def __init__(self, root=None):
        self.__root = None

    def BSTInsert(self, data, comp):
        if self.__root is None:
            self.__root = RedBlackTree(data, color=False)
        else:
            aux = self.__root
            while aux is not None:
                aux2 = aux
                if comp(aux.data.getVal(), data.getVal()) != -1:
                    aux = aux.__left
                else:
                    aux = aux.__right
            if comp(aux2.data.getVal(), data.getVal()) != -1:
                aux2.__left = RedBlackNode(data)
                return aux2.__left
            else:
                aux2.__right = RedBlackNode(data)
                return aux2.__right

    def fixInsertion(self, data, comp, node):
        parent_nd = None
        grand_parent_nd = None

        while (node != self.__root) and (node.color is not False) and (node.parent.color is True):
            
            

            
    def insert(self, data, comp):
        newnode = self.BSTInsert(data, comp)
        self.fixInsertion(data, comp, newnode)
        
