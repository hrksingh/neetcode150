# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNode = 0
        stack = [(root, root.val)]
        while stack:
            node, maxVal = stack.pop()
            if node.val >= maxVal:
                goodNode += 1
                maxVal = node.val
            if node.right:
                stack.append((node.right, maxVal))
            if node.left:
                stack.append((node.left, maxVal))
        return goodNode

    def goodNodesRecursive(self, root: TreeNode) -> int:
        def dfs(node, mv):
            res = 0
            if not node:
                return 0
            res = 1 if node.val >= mv else 0
            mv = max(mv, node.val)
            res += dfs(node.left, node.val)
            res += dfs(node.right, node.val)
            return res

        return dfs(root, root.val)

    def goodNodesRecursiveGlobal(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, mv):
            if not node:
                return
            if node.val >= mv:
                mv = node.val
                self.ans += 1
            dfs(node.left, mv)
            dfs(node.right, mv)

        dfs(root, root.val)
        return self.ans
