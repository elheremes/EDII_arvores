class LinkedList:
    # Métodos Padrões
    def __init__(self, data=None, nxt=None):
        self.__data = data
        self.__next = nxt

    ###########################################
    # Impressão                               #
    #                                         #
    # Método de imprimir a lista, ao chamar   #
    # no metodo print irá imprimir uma string #
    # no seguinte formato:                    #
    #                                         #
    #  n1_key --> n2_key --> ... --> nN_key   #
    #                                         #
    # Chamada: print(list_head)               #
    ###########################################
    def __str__(self):
        if self.__data is None:
            return "null"
        outstr = ""
        aux = self
        while aux is not None:
            outstr += str(aux.__data.getVal()) + " --> "
            aux = aux.__next
        outstr = outstr[0:len(outstr) - 5]
        return outstr

    ###################################
    # Inserção                        #
    #                                 #
    # Inserir dados na lista          #
    #                                 #
    # Chamada: list_head.insert(data) #
    ###################################
    def insert(self, data):
        if self.__data is None:
            self.__data = data
        else:
            aux = self
            while aux.__next is not None:
                aux = aux.__next
            newnode = LinkedList(data)
            aux.__next = newnode
        return True

    ##############################################
    # Remoção                                    #
    #                                            #
    # Remover dados da lista                     #
    #                                            #
    # Chamada: variavel = list_head.remove(data) #
    #                                            #
    # Caso não exista na lista irá retornar None #
    ##############################################
    def remove(self, key):
        if self.__data is None:
            return None
        elif self.__data.getVal() == key:
            data = self.__data
            if self.__next is not None:
                self.__data = self.__next.__data
                self.__next = self.__next.__next
            else:
                self.__data = None
            return data
        else:
            aux1 = self
            aux2 = self.__next
            while aux2 is not None:
                if aux2.__data.getVal() == key:
                    break
                aux1 = aux2
                aux2 = aux2.__next
            if aux2 is not None:
                data = aux2.__data
                aux1.__next = aux2.__next
                return data
            else:
                return None

    def search(self, key):
        if self.__data is None:
            return None
        else:
            aux = self
            while aux is not None:
                if aux.__data.getVal() == key:
                    return aux.__data
                aux = aux.__next
            return None
        
    def length(self):
        if self.__data is None:
            return 0
        else:
            cont = 1
            aux = self.__next
            while aux is not None:
                cont += 1
                aux = aux.__next
            return cont
