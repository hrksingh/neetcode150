# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minn, maxx):
            if not node:
                return True
            if not (minn < node.val < maxx):
                return False
            return dfs(node.left, minn, node.val) and dfs(node.right, node.val, maxx)

        return dfs(root, float("-inf"), float("inf"))

    def isValidBSTIterative(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        prev = float("-inf")

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()

            if node.val <= prev:
                return False

            prev = node.val
            curr = node.right

        return True
