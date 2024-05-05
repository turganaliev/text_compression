# read input file
file = open("input.txt", "r")
content = file.read()
print(content)
file.close()

# Identify all words in the text, assign a code to each
l = content.split()
d = {}
i = 1
for x in l:
    if x not in d:
        d[x] = i
        i += 1

print(d)
