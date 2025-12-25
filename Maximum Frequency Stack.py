class FreqStack:
    """A stack-like structure that pops the most frequent element.

    Internals:
    - `freq` maps value -> frequency count
    - `freq_stacks` maps frequency -> stack (list) of values with that frequency
    - `max_frequency` tracks the highest frequency currently present
    """

    def __init__(self):
        # value -> frequency
        self.freq: dict[int, int] = {}
        # highest frequency present in the stacks
        self.max_frequency: int = 0
        # frequency -> list of values (acting as stacks for each frequency)
        self.freq_stacks: dict[int, list[int]] = {}

    def push(self, val: int) -> None:
        """Push `val` onto the structure, updating its frequency and placing
        it on the corresponding frequency-stack.
        """
        new_count = 1 + self.freq.get(val, 0)
        self.freq[val] = new_count

        # If this is a new highest frequency, create its stack and update state
        if new_count > self.max_frequency:
            self.max_frequency = new_count
            self.freq_stacks[new_count] = []

        # push value onto the stack for its frequency
        self.freq_stacks.setdefault(new_count, []).append(val)

    def pop(self) -> int:
        """Pop and return the most frequent element. If multiple elements have
        the same frequency, the most recently pushed one is returned.
        """
        # pop from the stack corresponding to the current max frequency
        val = self.freq_stacks[self.max_frequency].pop()

        # decrement the frequency map
        self.freq[val] -= 1
        # if the stack for this frequency is now empty, decrease max_frequency
        if not self.freq_stacks[self.max_frequency]:
            self.max_frequency -= 1
        return val


if __name__ == "__main__":
    obj = FreqStack()
    pushes = [5, 7, 5, 7, 4, 5]
    for v in pushes:
        obj.push(v)

    pops = [obj.pop() for _ in range(4)]
    print("pops:", pops)  # expected: [5, 7, 5, 4]

    obj2 = FreqStack()
    for v in [1, 2, 2, 3, 3, 3]:
        obj2.push(v)
    print([obj2.pop() for _ in range(3)])  # expected: [3,3,3]
