from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # A None subRoot is technically always a subtree
        if not subRoot:
            return True
        # If root is None but subRoot isn't, it can't be a subtree
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    def isSubtreeMerkle(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        seen = set()
        self.merkle(root, seen)
        sub_hash = self.merkle(subRoot)
        return sub_hash in seen

    def merkle(self, node, seen=None):
        if not node:
            return hash(None)

        left_hash = self.merkle(node.left, seen)
        right_hash = self.merkle(node.right, seen)
        subtree_hash = hash((node.val, left_hash, right_hash))

        if seen is not None:
            seen.add(subtree_hash)
        return subtree_hash


def build_tree_from_list(values: list) -> Optional[TreeNode]:
    """Build a binary tree from a list using level-order (BFS) approach."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    solution = Solution()

    # Create trees from lists
    root = build_tree_from_list([1, 2, 3, 4, 5, None, None, 6])
    subRoot = build_tree_from_list([2, 4, 5])

    result = solution.isSubtree(root, subRoot)
    # resultM = solution.isSubtreeMerkle(root, subRoot)
    print(f"Is subRoot a subtree of root? {result}")

    root2 = build_tree_from_list([1, 2, 3, 4, 5])
    subRoot2 = build_tree_from_list([2, 4, 5])
    result2 = solution.isSubtree(root2, subRoot2)
    resultM = solution.isSubtreeMerkle(root2, subRoot2)
    print(f"Is subRoot a subtree of root? {result2}")
