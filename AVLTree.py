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

    # Getters
    # Altura
    def getHeight(self, node):
        if node is None:
            return -1
        else:
            return node.__height

    ###########################################
    # Inserção                                #
    #                                         #
    # Retorno: retorna a nova raiz atualizada #
    #                                         #
    # Chamada: root = root.insert(data)       #
    ###########################################
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

            balance = self.balance(self)

            if balance == 2:
                newBalance = self.balance(self.__right)
                if newBalance != -1:
                    return self.leftRotation()
                else:
                    return self.doubleLeftRotation()
            elif balance == -2:
                newBalance = self.balance(self.__left)
                if newBalance != 1:
                    return self.rightRotation()
                else:
                    return self.doubleRightRotation()

            return self

    #############################################
    # Remoção                                   #
    #                                           #
    # Retorno: retorna uma tupla (x, y) tal que #
    # x é a nova raiz e y o dado retirado       #
    #                                           #
    # Chamada: root, data = root.remove(key)    #
    #############################################
    def remove(self, key):
        dado = None
        root, dado = self.__remove(key, dado)
        return root, dado

    def __remove(self, key, data):
        if self.__data is None:
            return self, None
        else:
            if self.__data.getVal() > key:
                if self.__left is None:
                    return self, None
                else:
                    self.__left, data = self.__left.__remove(key, data)
            elif self.__data.getVal() < key:
                if self.__right is None:
                    return self, None
                else:
                    self.__right, data = self.__right.__remove(key, data)
            else:
                data = self.__data

                if self.__left is None:
                    return self.__right, data
                if self.__right is None:
                    return self.__left, data

                self.__data = self.__left.maxTree()
                aux = None
                self.__left, aux = self.__left.__remove(self.__data.getVal(),
                                                        aux)

            self.__height = 1 + max(self.getHeight(self.__left),
                                    self.getHeight(self.__right))

            balance = self.balance(self)

            if balance > 1 and self.balance(self.__left) >= 0:
                return self.leftRotation(), data
            # Case 2 - Right Right
            if balance < -1 and self.balance(self.__right) <= 0:
                return self.rightRotation(), data
            # Case 3 - Left Right
            if balance > 1 and self.balance(self.__left) < 0:
                return self.doubleLeftRotation(), data
            # Case 4 - Right Left
            if balance < -1 and self.balance(self.__right) > 0:
                return self.doubleRightRotation(), data

            return self, data

    ###############################################
    # Checar balanceamento                        #
    #                                             #
    # Retorno: retorna um inteiro que significa   #
    # a subtração do tamanho da subárvore direita #
    # menos o da subárvore esquerda               #
    #                                             #
    # Chamada = root.balance(root)                #
    ###############################################
    def balance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.__right) - self.getHeight(root.__left)

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
