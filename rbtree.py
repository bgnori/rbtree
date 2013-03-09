#!/usr/bin/python


LEFT  = -1
HIT = 0
RIGHT = 1

class NotFound(Exception):
    pass

class BinaryNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.rank = None # ugh!

    def visit(self, action, key):
        if key < self.key:
            if self.left is None:
                return action(self, LEFT, key)
            else:
                return self.left.visit(action, key)
        elif self.key < key:
            if self.right is None:
                return action(self, RIGHT, key)
            else:
                return self.right.visit(action, key)
        else:
            return action(self, HIT, key)

    def insert(self, key, value):
        def f(node, hand, key):
            if hand == LEFT:
                node.left = BinaryNode(key, value)
                return node.left
            elif hand == RIGHT:
                node.right = BinaryNode(key, value)
                return node.right
            else:
                return node

        node = self.visit(f, key)
        node.value = value

    def get(self, key):
        def f(node, hand, key):
            if hand == HIT:
                return node
            else:
                raise NotFound
        node = self.visit(f, key)
        return node.value

    def dump(self, count):
        if self.right:
            self.right.dump(count+1)
        print '   '*count, self.key, self.value
        if self.left:
            self.left.dump(count+1)



class BinaryTree:
    def __init__(self):
        self.root =  None

    def insert(self, key, value):
        if self.root is None:
            self.root = BinaryNode(key, value)
        else:
            self.root.insert(key, value)

    def key(self, key):
        if self.root is None:
            raise NotFound
        else:
            return self.root.get(key)

    def dump(self):
        if self.root:
            self.root.dump(0)



t = BinaryTree() 
for i, x in enumerate("binary tree example"):
    t.insert(x, i)


t.dump()
