from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


def build_tree_from_list(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None
    it = iter(vals)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for v in it:
        node = q.popleft()
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            q.append(node.right)
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    q = deque([root])
    out: List[Optional[int]] = []
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    # trim trailing Nones
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    vals = [4, 2, 7, 1, 3]
    val = 5
    root = build_tree_from_list(vals)
    print("before:", tree_to_list(root))
    root = Solution().insertIntoBST(root, val)
    print("after:", tree_to_list(root))
