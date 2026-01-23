# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            rightNode = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                rightNode = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        return res
