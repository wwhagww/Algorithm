class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def push(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            cur = self.root
            while True:
                if val < cur.key:
                    if cur.left is None:
                        cur.left = new_node
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = new_node
                        break
                    else:
                        cur = cur.right
    def postorder(self):
        stack = [(self.root, 0)]
        while stack:
            cur, state = stack.pop()
            if state == 0:
                stack.append((cur,1))
                if cur.right is not None:
                    stack.append((cur.right, 0))
                if cur.left is not None:
                    stack.append((cur.left, 0))
            else:
                print(cur.key)




import sys

lines = list(map(int, sys.stdin.readlines()))
tree = Tree()
for num in lines:
    tree.push(num)
tree.postorder()