# coding=utf-8

"""
author = Mateor
PYTHON 3.3.5
"""

from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)

import os
import aux
import Word as wd


class BTree(object):
  """A BTree implementation with search and insert functions. Capable of any order t."""

  class Node(object):
    """A simple B-Tree Node."""

    def __init__(self, t):
      self.keys = []
      self.children = []
      self.leaf = True
      # t is the order of the parent B-Tree. Nodes need this value to define max size and splitting.
      self._t = t

    def split(self, parent, payload, comp):
      """Split a node and reassign keys/children."""
      new_node = self.__class__(self._t)

      mid_point = self.size//2
      split_value = self.keys[mid_point]
      parent.add_key(split_value)

      # Add keys and children to appropriate nodes
      new_node.children = self.children[mid_point + 1:]
      self.children = self.children[:mid_point + 1]
      new_node.keys = self.keys[mid_point+1:]
      self.keys = self.keys[:mid_point]

      # If the new_node has children, set it as internal node
      if len(new_node.children) > 0:
        new_node.leaf = False

      parent.children = parent.add_child(new_node, comp)
      if comp(payload.getVal(), split_value.getVal()) == -1: # payload < split_value:
        return self
      else:
        return new_node

    @property
    def _is_full(self):
      return self.size == 2 * self._t - 1

    @property
    def size(self):
      return len(self.keys)

    def add_key(self, value):
      """Add a key to a node. The node will have room for the key by definition."""
      self.keys.append(value)
      self.keys.sort(key=lambda x: (x.getVal())[:aux.C])

    def add_child(self, new_node, comp):
      """
      Add a child to a node. This will sort the node's children, allowing for children
      to be ordered even after middle nodes are split.
      returns: an order list of child nodes
      """
      i = len(self.children) - 1
      while i >= 0 and comp(self.children[i].keys[0].getVal(), new_node.keys[0].getVal()) == 1: # self.children[i].keys[0] > new_node.keys[0]:
        i -= 1
      return self.children[:i + 1]+ [new_node] + self.children[i + 1:]


  def __init__(self, t):
    """
    Create the B-tree. t is the order of the tree. Tree has no keys when created.
    This implementation allows duplicate key values, although that hasn't been checked
    strenuously.
    """
    self._t = t
    if self._t <= 1:
      raise ValueError("B-Tree must have a degree of 2 or more.")
    self.root = self.Node(t)

  def insert(self, payload, comp):
    """Insert a new key of value payload into the B-Tree."""
    node = self.root
    # Root is handled explicitly since it requires creating 2 new nodes instead of the usual one.
    if node._is_full:
      new_root = self.Node(self._t)
      new_root.children.append(self.root)
      new_root.leaf = False
      # node is being set to the node containing the ranges we want for payload insertion.
      node = node.split(new_root, payload, comp)
      self.root = new_root
    while not node.leaf:
      i = node.size - 1
      while i > 0 and comp(payload.getVal(), node.keys[i].getVal()) == -1: # payload < node.keys[i] :
        i -= 1
      if comp(payload.getVal(), node.keys[i].getVal()) == 1: # payload > node.keys[i]:
        i += 1

      next = node.children[i]
      if next._is_full:
        node = next.split(node, payload, comp)
      else:
        node = next
    # Since we split all full nodes on the way down, we can simply insert the payload in the leaf.
    node.add_key(payload)

  def search(self, value, comp, node=None):
    """Return True if the B-Tree contains a key that matches the value."""
    if node is None:
      node = self.root
    for item in node.keys:
        if item.getVal() == value:
            return item
    #if value in node.keys:
     # return True
    if node.leaf:
      # If we are in a leaf, there is no more to check.
      return False
    else:
      i = 0
      while i < node.size and comp(value, node.keys[i].getVal()) == 1: # value > node.keys[i]:
        i += 1
      return self.search(value, node.children[i])

  def print_order(self):
    """Print an level-order representation."""
    this_level = [self.root]
    while this_level:
      next_level = []
      output = ""
      for node in this_level:
        if node.children:
          next_level.extend(node.children)
        output += str(node.keys) + " "
      print(output)
      this_level = next_level

      clear = lambda: os.system('clear')

  def __invertedIndex(self, node):
      if node.leaf:
          for obj in node.keys:
              print(obj)
      else:
          i = 0
          for obj in node.keys:
              self.__invertedIndex(node.children[i])
              print(obj)
              i += 1
          self.__invertedIndex(node.children[i])

  def invertedIndex(self):
      self.__invertedIndex(self.root)
     

if __name__ == '__main__' :   
  #clear()
  tree = BTree(3)
  dado1 = wd.Word("arroz", 1)
  dado2 = wd.Word("feijao", 2)
  dado3 = wd.Word("batata", 1)
  dado4 = wd.Word("cuzidao", 2)
  dado5 = wd.Word("muqueca", 1)
  dado6 = wd.Word("baiao", 2)

  tree.insert(dado1, aux.compWords)
  tree.insert(dado2, aux.compWords)
  tree.insert(dado3, aux.compWords)
  tree.insert(dado4, aux.compWords)
  tree.insert(dado5, aux.compWords)
  tree.insert(dado6, aux.compWords)

  tree.invertedIndex()

  eoq = tree.search("cuzidao", aux.compWords)

  print("\n", eoq)
  
  # while True:
  #  x = int(input("Insira na Arvore: "))
  #  tree.insert(x)
  #  tree.print_order()
