import LinkedList as ll
import numpy as np
import aux
import random
import Word as wd


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
        self.__keys = {}
        # O(size) aqui, tem como melhorar?
        aux = [ll.LinkedList() for i in range(self.__size)]
        self.__array = np.array(aux)
        
    def __setitem__(self, key, item):
        position = self.hashUniversal(key)
        if self.__array[position].search(key) is not None:
            self.__array[position].remove(key)
        self.__array[position].insert(HashElm(key, item))

    def __getitem__(self, key):
        if key not in self.__keys:
            return None
        position = self.__keys[key]
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
            position = self.__keys[word]
            value = self.__array[position].search(word)
            print(value.getItem())

    def isPrime(self, n):
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True

    def hashUniversal(self, key):
        k = ord(key[0])
        prime = k
        
        while prime < self.__size:
            prime += 1

        while not self.isPrime(prime):
            prime += 1

        a = random.randint(1, prime)
        b = random.randint(0, prime)

        h = ((a*k + b) % prime) % self.__size

        self.__keys[key] = h
        
        return h

            
    # Melhorar a função de hash, usar um Hash Universal
    def hash(self, key):
        return key % self.__size

    
if __name__ == '__main__':
    heshi = HashChained(30)
    
    dado1 = wd.Word("arroz", 1)
    dado2 = wd.Word("feijao", 2)
    dado3 = wd.Word("batata", 1)
    dado4 = wd.Word("cuzidao", 2)
    dado5 = wd.Word("muqueca", 1)
    dado6 = wd.Word("baiao", 2)

    heshi["arroz"] = dado1
    heshi["feijao"] = dado2
    heshi["batata"] = dado3
    heshi["cuzidao"] = dado4
    heshi["muqueca"] = dado5
    heshi["baiao"] = dado6

    print(heshi)
