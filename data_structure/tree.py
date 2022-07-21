# 트리 구조: 자료들 간의 계층 표현
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def setRoot(self, value):
        self.root = Node(value)

    def getRoot(self):
        if self.root is not None:
            return self.root
        else:
            return -1

    # 데이터의 대소 비교해서 정리
    def push(self, value):
        if self.root is None:
            self.setRoot(value)
        else:
            parent = tmp = self.root
            is_left_child = True
            while tmp is not None:
                parent = tmp
                if value < tmp.value:
                    tmp = tmp.left
                    is_left_child = True
                else:
                    tmp = tmp.right
                    is_left_child = False
            if is_left_child:
                parent.left = Node(value)
            else:
                parent.right = Node(value)

    def remove(self, value):
        if self.root is None:
            return False
        else:
            parent = ptr = self.root
            is_left_child = True
            while ptr is not None:
                parent = ptr
                if value == ptr.value:
                    break
                elif value < ptr.value:
                    ptr = ptr.left
                    is_left_child = True
                else:
                    ptr = ptr.right
                    is_left_child = False
            
            # 찾는 값이 트리 내에 없을 때
            if ptr is None:
                return False
            # 3가지 케이스 비교
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
                ptr.value = left.value
                if is_left_child:
                    parent.left = None
                else:
                    parent.right = None
        return True
    
    def Inorder(self, node):
        if node is not None:
            self.Inorder(node.left)
            print(f'{node.value} ->', end='')
            self.Inorder(node.right)
    
    def Preorder(self, node):
        if node is not None:
            print(f'{node.value} ->', end='')
            self.Preorder(node.left)
            self.Preorder(node.right)
    
    def Postorder(self, node):
        if node is not None:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(f'{node.value} ->', end='')






    

