class Node:
    """Node for doubly linked list"""

    __slots__ = ("key", "val", "next", "prev")

    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """
    LRU Cache implementation using HashMap + Doubly Linked List
    Time Complexity: O(1) for both get() and put()
    Space Complexity: O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes for easier insertion/deletion
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """Get value from cache and mark as recently used"""
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair in cache"""
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        """Remove node from doubly linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node: Node) -> None:
        """Insert node at the end (most recently used position)"""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def visualize(self) -> str:
        """Visualize the doubly linked list structure"""
        result = []

        # Header
        result.append("\n┌─── LRU Cache Visualization ───┐\n")
        result.append(
            f"│ Capacity: {self.capacity}  Size: {len(self.cache)}          │\n"
        )
        result.append("└───────────────────────────────┘\n")

        # Forward traversal
        result.append("Forward: HEAD ⇄ ")
        current = self.head.next
        nodes = []
        while current != self.tail:
            nodes.append(f"[{current.key}:{current.val}]")
            current = current.next

        if nodes:
            result.append(" ⇄ ".join(nodes))
        else:
            result.append("(empty)")
        result.append(" ⇄ TAIL\n")

        # LRU/MRU indicators
        if self.head.next != self.tail:
            result.append(
                f"\nLRU (Least Recently Used): [{self.head.next.key}:{self.head.next.val}]"
            )
            result.append(
                f"\nMRU (Most Recently Used):  [{self.tail.prev.key}:{self.tail.prev.val}]\n"
            )

        return "".join(result)


# ============= EXAMPLE USAGE =============

if __name__ == "__main__":
    cache = LRUCache(3)

    print(">>> cache.put(1, 1)")
    cache.put(1, 1)
    print(cache.visualize())

    print("\n>>> cache.put(2, 2)")
    cache.put(2, 2)
    print(cache.visualize())

    print("\n>>> cache.get(1)")
    print(f"Returns: {cache.get(1)}")
    print(cache.visualize())

    print("\n>>> cache.put(4, 4)  # Evicts key 2")
    cache.put(4, 4)
    print(cache.visualize())
