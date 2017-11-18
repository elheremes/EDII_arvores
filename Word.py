class Word:
    def __init__(self, word, occurs=3, c=3):
        self.__word = word
        self.__occurs = occurs

    def getVal(self):
        return self.__word

    # É pra ser outra estrutura de dados aqui
    def getOccurs(self):
        return self.__occurs

    
