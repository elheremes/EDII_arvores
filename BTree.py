class BTreeNode:
    def __init__(self, t):
	self.keys = []  # Array de Chaves
	self.kids = []  # Array de ponteiros que endereça os filhos
	self.t = t  # quantidade de chaves
	self.leaf = True  # Verdadeiro caso o nó seja folha

    def isFull(self):
	if self.size == ((2*self.t) - 1):
	    return True
	else:
	    return False

    def addKey(self, key):
	self.keys.append(key)
	self.keys.sort()

    def addKid(self, newNode):
	i = len(self.kids) - 1
		while i >= 0 and self.kids[i].keys[0] > newNode.keys[0]:
		    i -= 1

		#anexa o endereço de newNode na posição que repeite a ordem dos filhos 
		return self.kids[: i+1] + [newNode] + self.kids[i+1 :]

    def hasKid(self):
	if len(self.kids) > 0 :
	    return True
	else:
	    return False

    @property
    def size(self):
		return len(self.keys)

	#Função de dividir o nó quando encher
    def split(self, dad, element): 
	#1ª cria o novo pai e anexa o mediano no pai
	#Mesmo sendo filho, ainda tem todas as chaves e ponteiros
	#newNode
	newNode = BTreeNode(dad.t)
	newNode.leaf = dad.leaf
	indexMid = self.size//2
	median = self.keys[indexMid]
	dad.addKey(median)

		#translada as chaves e os filhos entre os irmão
		newNode.kids = self.kids[indexMid + 1 :]
		self.kids = self.kids[: indexMid + 1]
		newNode.keys = self.keys[indexMid + 1 :]
		self.keys = self.keys[: indexMid] #apenas até a metade pois: keys = t-1

		if newNode.hasKid() :
		    newNode.leaf = False

		dad.kids = dad.addKid(newNode)

		if element < median :
			return self
		else:
			return newNode

class BTree:
    def __init__(self, t):
		if t <= 0 :
			raise valueError("Número Negativo na criação da árvore.")

		self.root = BTreeNode(t)
		self.t = t

    def insert(self, element):
	#testar a capacidade 
	node = self.root

		if node.isFull():
		    newRoot = BTreeNode(self.t)
		    newRoot.leaf = False
		    newRoot.kids.append(node)
		    node.split(newRoot, element)
		    self.root = newRoot

		while not node.leaf:
		    i = (node.size - 1)
			while i > 0 and element < node.keys[i]:
			    i = i - 1

			if element > node.keys[i]:
			    i = i + 1

			son = node.kids[i]
			if son.isFull:
			    node = son.split(node, element)
			else:
			    node = son

		node.addKey(element)			

    def search(self, element):
		    pass

    def printTree(self):
	thisLevel = [self.root]
		while thisLevel :
		    nextLevel = []
		    output = ""

			for node in thisLevel :
				if node.kids :
				    nextLevel.extend(node.kids)
				    
				output += str(node.keys) + " "
				print(output)
				thisLevel = nextLevel
