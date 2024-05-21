





print("Running while loop")
x = 10
while x != 0:
    print(x)
    x = x-1







counts = dict()
line = input('Enter a line of text')
words = line.split()

print('Words',words)
print('counting....')

for word in words: 
    counts[word] = counts.get(word,0)+1
print('Counts',counts)


