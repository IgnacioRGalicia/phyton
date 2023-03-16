capi = input('Enter file name: ')
yeah = open(capi)
counts = dict()
for line in yeah:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for v, k in lst[:20]:
    print(k, v)