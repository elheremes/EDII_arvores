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
            parent_nd = node.parent
            grand_parent_nd = node.parent.parent

            if node.parent == grand_parent_nd.parent.left:
                uncle_nd = grand_parent_nd.right

                if uncle_nd is not None and uncle_nd.color == 1:
                    grand_parent_nd.color = 1
                    parent_nd.color = 0
                    uncle_nd.color = 0
                    node = grand_parent_nd
                else:
                    if node == parent_nd.right:
                        
    def rotateLeft(self, node):
        nd_right = node.right
        node.right = nd_right.left

        if node.right is not None:
            node.right.parent = node

        nd_right.parent = node.parent

        if node.parent is None:
            self.__root = nd_right
        elif node == node.parent.left:
            node.parent.left = nd_right
        else:
            node.parent.right = nd_right

        nd_right.left = node
        node.parent = nd_right

    def rotateRight(self, node):
        nd_left = node.left
        node.left = nd_left.right

        if node.left is not None:
            node.left.parent = node

        nd_left.parent = node.parent

        if node.parent is None:
            self.__root = nd_left
        elif node == node.parent.left:
            node.parent.left = nd_left
        else:
            node.parent.right = nd_left

        nd_left.right = node
        node.parent = nd_left
        
    def insert(self, data, comp):
        newnode = self.BSTInsert(data, comp)
        self.fixInsertion(data, comp, newnode)
        
