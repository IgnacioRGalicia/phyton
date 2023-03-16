print('Ex07_01')

fh = open('mbox-short.txt')
# print(fh)
# count = 0
# for lx in fh:
#     ly = lx.rstrip()
#     count = count + 1
#     print(ly.upper())
# print('there are', count, 'lines.')


# for lx in fh:
#     if lx.startswith('From: '):
#         lx = lx.rstrip()
#         if not lx.startswith('From: '):
#             continue
#         print(lx)

### Real 07 01
# for ul in fh:
#     ul = ul.rstrip()
#     print(ul.upper())
# end



# stuff = list()
# stuff.append(int(90))
# print(stuff)
# stuff.append('guacamallo')
# print(stuff)
# stuff.remove(90)
# print(stuff)

# for lx in fh:
#     if lx.startswith('From '):
#         lx = lx.rstrip()
#         if not lx.startswith('From '):
#             continue
#         words = lx.split()
#         print(words[2])
# Same as
for line in fh:
    
    line = line.rstrip()
    if line.startswith('From '):

        palabras = line.split()
    # This wouldve been a guardian but ive done it better xD
    # if len(palabras) < 1: # (Here you can strengh the guardian 
    # # by put a 3)
    #     continue
        print(palabras[2])