# tree: 자료들 간의 계층적 구조를 표현
# 이진 트리 구현, 노드로 표현
from dataclasses import dataclass

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def setRoot(self, data):
        self.root = Node(data)
    
    def getRoot(self):
        return self.root
    
    def push(self, data):
        node = Node(data)
        p = self.root
        if p is None:
            self.setRoot(data)
        else:
            ptrNode = self.root
            while ptrNode is not None:
                p = ptrNode
                if node.data < ptrNode.data:
                    ptrNode = ptrNode.left
                else:
                    ptrNode = ptrNode.right
            if node.data < p.data:
                p.left = node
            else:
                p.right = node
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    def preorder(self, node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def search(self, data):
        p = self.root
        while True:
            if p is None:
                return None
            elif p.data == data:
                return data
            elif data < p.data:
                p = p.left
            else:
                p = p.right
    
    def remove(self, data):
        ptr = self.root
        parent = None
        is_left_child = True # 부모의 왼쪽 자식인지 확인

        while True:
            if ptr is None:
                return False
            if data == ptr.data:
                break
            else:
                parent = ptr
                if data < ptr.data:
                    ptr = ptr.left
                    is_left_child = True
                else:
                    ptr = ptr.right
                    is_left_child = False
        
        if ptr.left is None:
            if ptr is self.root:
                self.root = ptr.right
            elif is_left_child:
                parent.left = ptr.right
            else:
                parent.right = ptr.right
        elif ptr.right is None:
            if ptr is self.root:
                self.root = ptr.left
            elif is_left_child:
                parent.left = ptr.left
            else:
                parent.right = ptr.left
        else:
            parent = ptr
            left = ptr.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            ptr.data = left.data
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True






    

