# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queuep = deque([p])
        arrayp = []

        while queuep:
            node = queuep.popleft()
            arrayp.append(node.val)

            if node.left:
                arrayp.append(node.left.val)
                queuep.append(node.left)
            else:
                arrayp.append(None)
            if node.right:
                arrayp.append(node.right.val)
                queuep.append(node.right)
            else:
                arrayp.append(None)


        queueq = deque([q])
        arrayq = []


        while queueq:
            node = queueq.popleft()
            arrayq.append(node.val)

            if node.left:
                arrayq.append(node.left.val)
                queueq.append(node.left)
            else:
                arrayq.append(None)
            if node.right:
                arrayq.append(node.right.val)
                queueq.append(node.right)
            else:
                arrayq.append(None)


        print(arrayq, arrayp)

        return arrayp == arrayq

        
        


        