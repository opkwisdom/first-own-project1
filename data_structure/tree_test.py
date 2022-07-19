from tree import BinarySearchTree as Tree

num = [3, 10, 2, 4, 8, 11]

newTree = Tree()
newTree.setRoot(7)

for i in num:
    newTree.push(i)

newTree.postorder(newTree.getRoot())
newTree.remove(3)
print()
newTree.postorder(newTree.getRoot())