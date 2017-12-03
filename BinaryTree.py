##########################################################
#   Arvore Genérica                                      #
#                                                        #
#   Necessário implementar um método getVal() no objeto  #
#   em que neste método se irá retornar a chave usada na #
#   árvore                                               #
##########################################################


class BinaryTree:
    # Métodos Padrões
    def __init__(self, data=None, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def __str__(self):
        return str(self.__data.getVal()) + "\n"

    # Métodos de Imprimir
    def preOrder(self):
        if self.__data is None:
            print("Árvore Vazia")
            return None
        if self.__left is not None:
            self.__left.preOrder()
        if self.__right is not None:
            self.__right.preOrder()
        print(self)

    def postOrder(self):
        if self.__data is None:
            print("Árvore Vazia")
            return None
        print(self)
        if self.__left is not None:
            self.__left.postOrder()
        if self.__right is not None:
            self.__right.postOrder()

    def simmetric(self):
        if self.__data is None:
            print("Árvore Vazia")
            return None
        if self.__left is not None:
            self.__left.simmetric()
        print(self)
        if self.__right is not None:
            self.__right.simmetric()

    def invertedIndex(self):
        if self.__data is None:
            print("Árvore Vazia")
            return None
        if self.__left is not None:
            self.__left.invertedIndex()
        print(self.__data)
        if self.__right is not None:
            self.__right.invertedIndex()
            
    # Altura
    def height(self):
        if self.__left is None and self.__right is None:
            return 0  # Mudado aqui
        else:
            hl = 0
            hr = 0
            if self.__left is not None:
                hl = self.__left.height()
            if self.__right is not None:
                hr = self.__right.height()
            if hl > hr:
                return 1 + hl
            else:
                return 1 + hr

    # Inserção e Remoção
    def insert(self, data, comp):
        if self.__data is None:
            self.__data = data
        else:
            aux = None
            aux2 = self
            while aux2 is not None:
                aux = aux2
                if comp(aux2.__data.getVal(), data.getVal()) == 1:
                    aux2 = aux2.__left
                else:
                    aux2 = aux2.__right
            if comp(aux.__data.getVal(), data.getVal()) == 1:
                aux.__left = BinaryTree(data)
            else:
                aux.__right = BinaryTree(data)

    def remove(self, key, comp):
        if self.__data is None:
            return None
        if self.__data is not None:
            if comp(self.__data.getVal(), key) == 0:
                data = self.__data
                if self.__left is not None:
                    self.__data = self.remove(self.__left.maxTree().getVal(),
                                              comp)
                elif self.__right is not None:
                    self.__data = self.remove(self.__right.minTree().getVal(),
                                              comp)
                else:
                    self.__data = None
                return data
        aux = None
        aux2 = self
        while aux2 is not None:
            if comp(aux2.__data.getVal(), key) == 0:
                break
            aux = aux2
            if comp(aux2.__data.getVal(), key) == 1:
                aux2 = aux2.__left
            else:
                aux2 = aux2.__right
        if aux2 is not None:
            data = aux2.__data
            if aux2.__left is None and aux2.__right is None:
                if aux.__left == aux2:
                    aux.__left = None
                else:
                    aux.__right = None
            elif aux2.__left is None and aux2.__right is not None:
                if aux.__left == aux2:
                    aux.__left = aux2.__right
                else:
                    aux.__right = aux2.__right
            elif aux2.__left is not None and aux2.__right is None:
                if aux.__left == aux2:
                    aux.__left = aux2.__left
                else:
                    aux.__right = aux2.__left
            else:
                aux2.__data = aux2.remove(aux2.__left.maxTree().getVal(), comp)
            return data

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
    def search(self, key, comp):
        aux = self
        while aux is not None:
            if comp(aux.__data.getVal(), key) == 0:
                return aux.__data
            if comp(aux.__data.getVal(), key) == 1:
                aux = aux.__left
            else:
                aux = aux.__right
