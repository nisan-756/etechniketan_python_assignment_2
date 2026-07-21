strings = ["aba", "abc", "1991", "madam", "hi", "python", "level"]

count = 0

for s in strings:
    if len(s) > 2 and s == s[::-1]:
        count += 1

print("Number of palindromes:", count)