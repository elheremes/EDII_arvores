class FilesOccur:
    def __init__(self, fileId, occur=0):
        self.occur = occur
        self.fileId = fileId

    def getOccur(self):
        return self.occur

    def getFileId(self):
        return self.fileId

    def incrementOccur(self):
        self.occur = self.occur + 1
        
    
class Word:
    def __init__(self, word, qntdFiles=1):
        self.__word = word
        self.__occurs = [FilesOccur(i+1) for i in range(qntdFiles)]

    def __str__(self):
        return self.__word + " " + self.printOccurs()

    def getVal(self):
        return self.__word

    # É pra ser outra estrutura de dados aqui
    def getOccurs(self):
        return self.__occurs

    def incrementOccurs(self, fileId):
        self.__occurs[fileId - 1].incrementOccur()

    def printOccurs(self):
        string = ""

        self.__occurs.sort(key=lambda x: x.occur)
        
        for fOccurs in self.__occurs:
            if fOccurs.occur == 0:
                continue
            string += str(fOccurs.occur) + " " + str(fOccurs.fileId) + ", "

        string = string[:len(string)-2]
            
        return string

