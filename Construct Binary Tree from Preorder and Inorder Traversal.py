from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


def print_tree(
    node: Optional[TreeNode], prefix: str = "", is_left: bool = True
) -> None:
    if node is None:
        return
    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    preorder = [40, 20, 10, 30, 60, 50, 70]
    inorder = [10, 20, 30, 40, 50, 60, 70]
    root = Solution().buildTree(preorder, inorder)
    print_tree(root)
