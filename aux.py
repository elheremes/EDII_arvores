import Word as wd
import re
import BinaryTree as bt
import AVLTree as avl
import RedBlackTree as rbt
import HashChained as hc

C = 0


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
    C = int(input("Digite o valor do parâmetro C: "))

    words = {}
    i = 1
    for fil in files:
        f = open(fil, "r")
        for line in f:
            for word in re.split('; |, |\*|\n|;|!|\?| ', line):
                if len(word) < C:
                    continue
                if word.lower() not in words:
                    words[word.lower()] = wd.Word(word.lower(), len(files))
                words[word.lower()].incrementOccurs(i)
        i = i + 1
        f.close()
        
    return words


def loadBinaryTree(words):
    tree = bt.BinaryTree()
    
    for key, word in words.items():
        tree.insert(word, comp)

    return tree


def loadAVLTree(words):
    tree = avl.AVLTree()

    for key, word in words.items():
        tree = tree.insert(word, comp)

    return tree


def loadRedBlackTree(words):
    tree = rbt.RedBlackTree()

    for key, word in words.items():
        tree.insert(word, comp)

    return tree


def loadHash(words):
    hashi = hc.HashChained(20)  # melhorar isso aqui!

    for key, word in words.items():
        hashi[key] = word

    return hashi


def loadBTree(words):
    # B Tree com problemas!
    return True
