import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root is not None:
            q = Queue()
            q.enqueue(root)
            order = []

            while not q.is_null():
                curr = q.dequeue()
                order.append(curr.data)

                if curr.left is not None:
                    q.enqueue(curr.left)
                if curr.right is not None:
                    q.enqueue(curr.right)

            print(" ".join(map(str,order)))

        #Write your code here

class Queue:
    def __init__(self):
        self.queue = []

    def is_null(self):
        if len(self.queue) != 0:
            return False
        else:
            return True

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return None

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
