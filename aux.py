import Word as wd
import re
import unidecode as un
import BinaryTree as bt
import AVLTree as avl
import RedBlackTree as rbt
import HashChained as hc
import BTree as b
import math

C = 4
dTerms = {}


def comp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0


def compWords(x, y):
    global C
    if x[0:C] > y[0:C]:
        return 1
    elif x[0:C] < y[0:C]:
        return -1
    return 0


def loadWords(files):
    global C
    global dTerms
    C = int(input("Digite o valor do parâmetro C: "))

    words = {}
    i = 1
    for fil in files:
        f = open(fil, "r")
        dTerms[fil] = 0
        fileWords = {}
        for line in f:
            for word in re.split('; |, |\*|\n|;|!|\?|\.| ', line):
                if len(word) < C:
                    continue
                theWord = un.unidecode(word.lower())
                if theWord not in words:
                    words[theWord] = wd.Word(theWord, len(files))
                if theWord not in fileWords:
                    fileWords[theWord] = theWord
                    dTerms[fil] += 1
                words[theWord].incrementOccurs(i)
        i = i + 1
        f.close()
    
    return words


def loadBinaryTree(words):
    tree = bt.BinaryTree()
    
    for key, word in words.items():
        tree.insert(word, compWords)

    return tree


def loadAVLTree(words):
    tree = avl.AVLTree()

    for key, word in words.items():
        tree = tree.insert(word, compWords)

    return tree


def loadRedBlackTree(words):
    tree = rbt.RedBlackTree()

    for key, word in words.items():
        tree.insert(word, compWords)

    return tree


def loadHash(words):
    hashSize = int(input("Digite o tamanho do hash: "))
    
    hashi = hc.HashChained(hashSize)  # melhorar isso aqui!

    for key, word in words.items():
        hashi[key] = word

    return hashi


def loadBTree(words):
    grau = int(input("Informe o grau da arvore: "))
    tree = b.BTree(grau)

    for key, word in words.items():
        tree.insert(word, compWords)
    
    return tree


# Defimir limiar
def IDF(files, tad, tadStr):
    global dTerms
    N = len(files)
    L = 0.05
    
    strtermos = str(input("Insira os termos da consulta: "))
    termos = strtermos.split()

    i = 0
    weights = []
    for termo in termos:
        if tadStr == "hash":
            word = tad[termo]
        else:
            word = tad.search(termo, compWords)
        fN = 1
        weights.append([])
        if word is None:
            for fil in files:
                weights[i].append(0)
            continue
        dj = word.getQFilesWOccurs(termo)
        for fil in files:
            f = word.getOccursFile(fN)
            weights[i].append(f * (math.log(N, 2)/dj))
            fN += 1
        i += 1

    IDF = []
    fN = 1
    for fil in files:
        tSum = 0
        i = 0
        for item in termos:
            tSum += weights[i][fN-1]
            i += 1
        IDF.append((1/dTerms[fil]) * tSum)
        fN += 1

    IDFcpy = list(IDF)
    IDF.sort(reverse=True)
    
    for idf_term in IDF:
        if idf_term < L:
            continue
        i = IDFcpy.index(idf_term)
        print(files[i], idf_term)
