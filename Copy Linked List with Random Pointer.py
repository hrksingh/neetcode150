from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        oldToCopy: dict[Optional[Node], Optional[Node]] = {None: None}

        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]


def build_random_list(data: list[tuple[int, Optional[int]]]) -> Optional[Node]:
    """Build a random-pointer linked list from array of [val, random_index_or_None].

    Example input: [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    """
    if not data:
        return None
    nodes: list[Node] = [Node(val) for val, _ in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_val, rnd) in enumerate(data):
        nodes[i].random = nodes[rnd] if (rnd is not None) else None
    return nodes[0]


def serialize_random_list(head: Optional[Node]) -> list[list[object]]:
    """Serialize list to [[val, random_index_or_None], ...] for easy comparison.
    random_index uses the node index in the list (0-based).
    """
    nodes: list[Node] = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    node_to_idx = {n: i for i, n in enumerate(nodes)}
    out: list[list[object]] = []
    for n in nodes:
        if n.random is None:
            rnd_idx = None
        else:
            rnd_idx = node_to_idx[n.random]
        out.append([n.val, rnd_idx])
    return out


def __node_repr(node: Optional[Node]) -> str:
    if node is None:
        return "None"
    rnd = node.random.val if node.random else None
    return f"Node(val={node.val}, random={rnd})"


if __name__ == "__main__":
    data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = build_random_list(data)
    print("original ->", serialize_random_list(head))
    copied = Solution().copyRandomList(head)
    print("copied   ->", serialize_random_list(copied))
