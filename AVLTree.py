class AVLTree:
    # Métodos Padrões
    def __init__(self, data=None, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
        self.__height = 0

    def __str__(self):
        return str(self.__data.getVal()) + "\n"

    # Métodos de Imprimir
    def preOrder(self):
        if self.__left is not None:
            self.__left.preOrder()
        if self.__right is not None:
            self.__right.preOrder()
        print(self)

    def postOrder(self):
        print(self)
        if self.__left is not None:
            self.__left.postOrder()
        if self.__right is not None:
            self.__right.postOrder()

    def simmetric(self):
        if self.__left is not None:
            self.__left.simmetric()
        print(self)
        if self.__right is not None:
            self.__right.simmetric()

    # Altura
    def getHeight(self, node):
        if node is None:
            return -1
        else:
            return node.__height

    # Inserção e Remoção        
    def insert(self, data):
        if self.__data is None:
            self.__data = data
            
        else:
            if self.__data.getVal() > data.getVal():
                if self.__left is not None:
                    self.__left = self.__left.insert(data)
                else:
                    self.__left = AVLTree(data)
            else:
                if self.__right is not None:
                    self.__right = self.__right.insert(data)
                else:
                    self.__right = AVLTree(data)

            self.__height = 1 + max(self.getHeight(self.__left),
                                    self.getHeight(self.__right))

            balance = self.balance()
            
            if balance == 2:
                newBalance = self.__right.balance()
                if newBalance != -1:
                    return self.leftRotation()
                else:
                    return self.doubleLeftRotation()
            elif balance == -2:
                newBalance = self.__left.balance()
                if newBalance != 1:
                    return self.rightRotation()
                else:
                    return self.doubleRightRotation()
                
            return self

    def balance(self):
        return self.getHeight(self.__right) - self.getHeight(self.__left)
    
    def remove(self, key, data):
        if self.__data is None:
            return self, None
        else:
            if self.__data.getVal() > key:
                if self.__left is None:
                    return self, None
                else:
                    self.__left, data = self.__left.remove(key, data)
            elif self.__data.getVal() < key:
                if self.__right is None:
                    return self, None
                else:
                    self.__right, data = self.__right.remove(key, data)
            else:
                data = self.__data

                if self.__left is None:
                    return self.__right, data
                if self.__right is None:
                    return self.__left, data

                self.__data = self.__left.maxTree()
                aux = None
                self.__left, aux = self.__left.remove(self.__data.getVal(),
                                                       aux)

            self.__height = 1 + max(self.getHeight(self.__left),
                                    self.getHeight(self.__right))

            balance = self.balance()
            
            if balance > 1 and self.__left.balance() >= 0:
                return self.leftRotation(), data
            # Case 2 - Right Right
            if balance < -1 and self.__right.balance() <= 0:
                return self.rightRotation(), data
            # Case 3 - Left Right
            if balance > 1 and self.__left.balance() < 0:
                return self.doubleLeftRotation(), data
            # Case 4 - Right Left
            if balance < -1 and self.__right.balance() > 0:
                return self.doubleRightRotation(), data
            
            return self, data

            
    # Máximos e Mínimos
    def maxTree(self):
        aux = self
        while aux.__right is not None:
            aux = aux.__right
        return aux.__data

    def minTree(self):
        aux = self
        while aux.__left is not None:
            aux = aux.__left
        return aux.__data

    # Busca
    def search(self, key):
        aux = self
        while aux is not None:
            if aux.__data.getVal() == key:
                return aux.__data
            if aux.__data.getVal() > key:
                aux = aux.__left
            else:
                aux = aux.__right

    # Rotações
    def leftRotation(self):
        aux = self.__right
        self.__right = aux.__left
        aux.__left = self

        self.__height = max(self.getHeight(self.__left),
                            self.getHeight(self.__right)) + 1

        aux.__height = max(aux.getHeight(aux.__right), self.__height) + 1
        
        return aux

    def rightRotation(self):
        aux = self.__left
        self.__left = aux.__right
        aux.__right = self

        self.__height = max(self.getHeight(self.__left),
                            self.getHeight(self.__right)) + 1

        aux.__height = max(aux.getHeight(aux.__left), self.__height) + 1
        
        return aux

    def doubleRightRotation(self):
        self.__left = self.leftRotation()
        return self.rightRotation()

    def doubleLeftRotation(self):
        self.__right = self.rightRotation()
        return self.leftRotation()
