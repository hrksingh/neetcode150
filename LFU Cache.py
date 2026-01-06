from collections import defaultdict


class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.val = value
        self.counter = 1
        self.next: Node | None = None
        self.prev: Node | None = None


class Dll:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        nxt_node = self.head.next

        node.next = nxt_node
        node.prev = self.head

        self.head.next = node
        nxt_node.prev = node
        self.size += 1

    def remove(self, node):
        nxt_node = node.next
        prev_node = node.prev

        prev_node.next = nxt_node
        nxt_node.prev = prev_node

        self.size -= 1

    def remove_last(self) -> Node | None:
        if self.size > 0:
            node = self.tail.prev
            self.remove(node)
            return node
        return None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.cache = {}  # key -> Node
        self.freq_to_dll = defaultdict(Dll)  # freq -> DLL

    def _update_freq(self, node: Node):
        freq = node.counter
        self.freq_to_dll[freq].remove(node)

        if self.freq_to_dll[freq].size == 0:
            del self.freq_to_dll[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        node.counter += 1
        self.freq_to_dll[node.counter].add(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update_freq(node)
            return

        if len(self.cache) >= self.capacity:
            evict_node = self.freq_to_dll[self.min_freq].remove_last()
            del self.cache[evict_node.key]

        node = Node(key, value)
        self.cache[key] = node
        self.freq_to_dll[1].add(node)
        self.min_freq = 1


#### Tests ###
def test_lfu_cache():
    """Test LFU Cache implementation with assertions"""

    # Test Case 1: Basic operations
    print("Test Case 1: Basic LFU operations")
    lfu = LFUCache(2)

    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1, "Failed: get(1) should return 1"
    print("✓ put(1,1), put(2,2), get(1) = 1")

    lfu.put(3, 3)
    assert lfu.get(2) == -1, "Failed: key 2 should be evicted"
    print("✓ put(3,3) evicted key 2, get(2) = -1")

    assert lfu.get(3) == 3, "Failed: get(3) should return 3"
    print("✓ get(3) = 3")

    lfu.put(4, 4)
    assert lfu.get(1) == -1, "Failed: key 1 should be evicted"
    assert lfu.get(3) == 3, "Failed: get(3) should return 3"
    assert lfu.get(4) == 4, "Failed: get(4) should return 4"
    print("✓ put(4,4) evicted key 1, get(1) = -1, get(3) = 3, get(4) = 4")

    print()

    # Test Case 2: Update existing key
    print("Test Case 2: Update existing key")
    lfu2 = LFUCache(2)
    lfu2.put(1, 1)
    lfu2.put(2, 2)
    lfu2.put(1, 10)  # Update key 1
    assert lfu2.get(1) == 10, "Failed: updated value should be 10"
    print("✓ put(1,1), put(2,2), put(1,10), get(1) = 10")

    lfu2.put(3, 3)
    assert lfu2.get(2) == -1, "Failed: key 2 should be evicted"
    assert lfu2.get(1) == 10, "Failed: key 1 should still exist"
    print("✓ put(3,3) evicted key 2, get(2) = -1, get(1) = 10")

    print()

    # Test Case 3: Frequency tracking
    print("Test Case 3: Frequency tracking")
    lfu3 = LFUCache(3)
    lfu3.put(1, 10)
    lfu3.put(2, 20)
    lfu3.put(3, 30)

    lfu3.get(1)  # freq: 1->2
    lfu3.get(2)  # freq: 2->2
    lfu3.get(1)  # freq: 1->3

    lfu3.put(4, 40)  # Should evict key 3 (freq=1)
    assert lfu3.get(3) == -1, "Failed: key 3 should be evicted (lowest freq)"
    assert lfu3.get(1) == 10, "Failed: key 1 should exist (highest freq)"
    assert lfu3.get(2) == 20, "Failed: key 2 should exist"
    assert lfu3.get(4) == 40, "Failed: key 4 should exist"
    print("✓ Correctly evicted least frequently used key (key 3)")

    print()

    # Test Case 4: Zero capacity
    print("Test Case 4: Zero capacity")
    lfu4 = LFUCache(0)
    lfu4.put(1, 1)
    assert lfu4.get(1) == -1, "Failed: zero capacity cache should not store anything"
    print("✓ Zero capacity cache returns -1 for all gets")

    print()

    # Test Case 5: Single capacity
    print("Test Case 5: Single capacity")
    lfu5 = LFUCache(1)
    lfu5.put(1, 1)
    assert lfu5.get(1) == 1, "Failed: should return 1"
    lfu5.put(2, 2)
    assert lfu5.get(1) == -1, "Failed: key 1 should be evicted"
    assert lfu5.get(2) == 2, "Failed: should return 2"
    print("✓ Single capacity cache works correctly")

    print()
    print("=" * 50)
    print("All tests passed! ✅")
    print("=" * 50)


if __name__ == "__main__":
    test_lfu_cache()