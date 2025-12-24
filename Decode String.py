class Solution:
    def decodeString(self, s: str) -> str:
        """Decode strings with nested repeats like '3[a2[c]]' -> 'accaccacc'."""
        stack: list[str] = []

        for ch in s:
            if ch != "]":
                # push characters and markers onto the stack until a closing bracket
                stack.append(ch)
            else:
                # build the substring inside the matching '['
                substr_chars: list[str] = []
                while stack and stack[-1] != "[":
                    substr_chars.append(stack.pop())
                # remove the '['
                stack.pop()

                # collect the repeat count (may be multiple digits)
                digits: list[str] = []
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())

                repeat = int("".join(reversed(digits))) if digits else 1
                decoded = "".join(reversed(substr_chars)) * repeat
                # push the decoded substring back onto the stack as one element
                stack.append(decoded)

        # join all parts into the final decoded string
        return "".join(stack)


if __name__ == "__main__":
    s = "2[abc]3[cd]ef"
    expected_output = "abcabccdcdcdef"
    output = Solution().decodeString(s)

    print(output)
    print(output == expected_output)
