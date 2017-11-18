import LinkedList as ll


class HashChained:
    def __init__(self, size):
        if size <= 0:
            size = 10
        self.__size = size
        self.__array = [ll.LinkedList() for i in range(self.__size)]

    def __setitem__(self, key, item):
        position = self.hash(len(key))
        self.__array[position].insert(item)

    def __getitem__(self, key):
        position = self.hash(key)
        return self.__array[position]

    def __str__(self):
        outstr = ""
        for i in range(self.__size):
            outstr += self.__array[i].__str__() + "\n"
        return outstr
            
    def hash(self, key):
        return key % self.__size
