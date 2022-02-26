import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        queue = list()
        nodes_traversed = ''
        queue.append(root)
        while len(queue) is not 0:
            current_node = queue.pop(0)
            if current_node.left: queue.append(current_node.left)
            if current_node.right: queue.append(current_node.right)
            nodes_traversed += str(current_node.data)+ " "

        print(nodes_traversed)


# Write your code here


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
