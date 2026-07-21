s1 = input("Enter a string: ")

char_count = {}

for ch in s1:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print(char_count)