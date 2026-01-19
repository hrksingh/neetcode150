# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestorRecursive(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorRecursive(root.right, p, q)  # type: ignore
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorRecursive(root.left, p, q)  # type: ignore
        return root

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:  # type: ignore
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr


if __name__ == "__main__":
    # build sample BST:
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n8 = TreeNode(8)
    n0 = TreeNode(0)
    n4 = TreeNode(4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n6.left, n6.right = n2, n8
    n2.left, n2.right = n0, n4
    n4.left, n4.right = n3, n5
    n8.left, n8.right = n7, n9

    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0   4 7   9
    #       / \
    #      3   5

    sol = Solution()

    # example 1: LCA of 2 and 8 is 6
    lca = sol.lowestCommonAncestor(n6, n2, n8)
    lcar = sol.lowestCommonAncestorRecursive(n6, n2, n8)
    print("LCA:", lca.val)
    print("LCAR:", lcar.val)

    # example 2: LCA of 2 and 4 is 2
    lca = sol.lowestCommonAncestor(n6, n2, n4)
    lcar = sol.lowestCommonAncestorRecursive(n6, n2, n4)
    print("LCA:", lca.val)
    print("LCAR:", lcar.val)
