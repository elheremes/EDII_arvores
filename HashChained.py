import LinkedList as ll
import numpy as np
import aux


class HashElm:
    def __init__(self, key, item):
        self.key = key
        self.item = item

    def getItem(self):
        return self.item

    def getVal(self):
        return self.key

    #  def getValC(self):
    #   return self.key[:aux.C]


class HashChained:
    def __init__(self, size):
        if size <= 0:
            size = 10
        self.__size = size
        # O(size) aqui, tem como melhorar?
        aux = [ll.LinkedList() for i in range(self.__size)]
        self.__array = np.array(aux)
        
    def __setitem__(self, key, item):
        position = self.hash(len(key))
        if self.__array[position].search(key) is not None:
            self.__array[position].remove(key)
        self.__array[position].insert(HashElm(key, item))

    def __getitem__(self, key):
        position = self.hash(len(key))
        elm = self.__array[position].search(key)
        if elm is not None:
            return elm.getItem()
        return None
    
    def __str__(self):
        outstr = ""
        for i in range(self.__size):
            outstr += self.__array[i].__str__() + "\n"
        return outstr

    def invertedIndex(self, words):
        keyLists = list(words.keys())
        keyLists.sort(key=lambda x: x[:aux.C])
    
        for word in keyLists:
            position = self.hash(len(word))
            value = self.__array[position].search(word)
            print(value.getItem())

    # Melhorar a função de hash, usar um Hash Universal
    def hash(self, key):
        return key % self.__size
