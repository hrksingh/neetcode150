class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []
        for part in parts:
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)


path = "/neetcode/practice//...///../courses"
print(Solution().simplifyPath(path))
