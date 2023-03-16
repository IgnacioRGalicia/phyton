print('Ex09')

text = open('mbox-short.txt')

counts = {} # or dict()

for line in text:
    
    line = line.rstrip()
    words = line.split()
    # print('Words:', words)

    # print('Counting...')
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    # print('Counts', counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)