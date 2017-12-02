class FilesOccur:
    def __init__(self, fileId, occur=0):
        self.__occur = occur
        self.__fileId = fileId

    def getOccur(self):
        return self.__occur

    def getFileId(self):
        return self.__fileId

    def incrementOccur(self):
        self.__occur = self.__occur + 1
        
    
class Word:
    def __init__(self, word, qntdFiles):
        self.__word = word
        self.__occurs = [FilesOccur(i) for i in range(qntdFiles)]

    def __str__(self):
        return self.__word + " | Occur: " + str(self.__occurs)

    def getVal(self):
        return self.__word

    # É pra ser outra estrutura de dados aqui
    def getOccurs(self):
        return self.__occurs

    def incrementOccurs(self, fileId):
        self.__occurs[fileId - 1].incrementOccur()

