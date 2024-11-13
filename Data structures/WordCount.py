import os

# Get the absolute path
file_path = os.path.abspath("Poem.txt")
print(f"Trying to open file at: {file_path}")

word_count = {}

word_count["Ashish"] = 1

with open("Data structures\Poem.txt","r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace("\n", "").replace(".", "").replace(";", "").replace(",", "").replace("\"", "")
            if token in word_count:
                word_count[token]+=1
            else:
                word_count[token] = 1

print(word_count)