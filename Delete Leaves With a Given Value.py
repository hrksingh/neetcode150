from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root


if __name__ == "__main__":
    data = [1, 2, 3, 2, None, 2, 4]
    target = 2

    def build_tree(values):
        if not values:
            return None
        nodes = [None if v is None else TreeNode(v) for v in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    def tree_to_list(root):
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            node = q.popleft()
            if node:
                out.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                out.append(None)
        # Trim trailing Nones
        while out and out[-1] is None:
            out.pop()
        return out

    root_node = build_tree(data)
    res_node = Solution().removeLeafNodes(root_node, target)
    print(tree_to_list(res_node))
