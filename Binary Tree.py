from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


# --- Data Setup ---
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("========== Recursive Traversal===========")


def in_order(node: TreeNode):
    if not node:
        return
    in_order(node.left)  # pyright: ignore[reportArgumentType]
    print(node, end=" ")
    in_order(node.right)  # pyright: ignore[reportArgumentType]


def pre_order(node: TreeNode):
    if not node:
        return
    print(node, end=" ")
    pre_order(node.left)  # pyright: ignore[reportArgumentType]
    pre_order(node.right)  # pyright: ignore[reportArgumentType]


def post_order(node: TreeNode):
    if not node:
        return
    post_order(node.left)  # pyright: ignore[reportArgumentType]
    post_order(node.right)  # pyright: ignore[reportArgumentType]
    print(node, end=" ")


print("========== In-Order ===========")
in_order(root)

print("\n========== Pre-Order ===========")
pre_order(root)

print("\n========== Post-Order ==========")
post_order(root)


print("\n========== Iterative Traversal===========")


def pre_order_iterative(node: TreeNode):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node, end=" ")
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)


print("========== Pre Order Iterative ===========")
pre_order_iterative(root)


def post_order_Iterative(root: TreeNode):
    stack = []
    curr, last_visited = root, None

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek_node = stack[-1]

            if peek_node.right and last_visited != peek_node.right:
                curr = peek_node.right
            else:
                print(peek_node, end=" ")
                last_visited = stack.pop()


print("\n========== Post Order Iterative Approach 1 ===========")
post_order_Iterative(root)


def post_order_Iterative_2(root: TreeNode):
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                print(node, end=" ")
            else:
                stack.append((node, True))
                stack.append((node.right, False))  # type: ignore
                stack.append((node.left, False))  # type: ignore


print("\n========== Post Order Iterative Approach 2 ===========")
post_order_Iterative_2(root)


def in_order_Iterative_flagged(root: TreeNode):
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if not node:
            continue

        if visited:
            print(node, end=" ")
        else:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))


print("\n========== In Order Iterative Approach 1===========")
in_order_Iterative_flagged(root)


def in_order_iterative(root):
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.val, end=" ")
        curr = curr.right


print("\n========== In Order Iterative Approach 1===========")
in_order_iterative(root)


print("========== Level Order Traversal===========")


def level_order(root: TreeNode):
    q = deque([root])

    while q:
        node = q.popleft()
        print(node, end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


print("\n========== Level Order Approach(BFS)===========")
level_order(root)
