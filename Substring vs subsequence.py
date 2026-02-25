x = "abcd"
n = len(x)

substring = []
subsequence = [""]


for i in range(n):
    for j in range(i + 1, n + 1):
        substring.append(x[i:j])


for char in x:
    current_count = len(subsequence)
    for i in range(current_count):
        new_sub = subsequence[i] + char
        subsequence.append(new_sub)

print(f"substring: {substring}")
print(f"subsequence: {subsequence}")
