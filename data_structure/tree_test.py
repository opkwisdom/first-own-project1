# 첫번째 트리
from tree import BinarySearchTree as Tree
import numpy as np

newTree = Tree()
newTree.setRoot(20)

num = np.random.randint(1, 40, 10)
for i in num:
    newTree.push(i)

print(num)
rootNode = newTree.getRoot()
print("Inorder")
newTree.Inorder(rootNode)
print()
print("Preorder")
newTree.Preorder(rootNode)
print()
print("Postorder")
newTree.Postorder(rootNode)
print()