s1 = "practice is important to perfectly learn python"

indexes = []

for i in range(len(s1)):
    if s1[i] == "p":
        indexes.append(i)

print(indexes)