# read input file
file = open("input.txt", "r")
content = file.read()
print(content)
file.close()

# Identify all words in the text, assign a code to each
l = content.split()
print(l)
d = {}
i = 1
for word in l:
    if word not in d:
        d[word] = i
        i += 1
