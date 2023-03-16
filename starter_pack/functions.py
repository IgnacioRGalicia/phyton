# porcion en el que al dar un dato procesa y da una respuesta

# definicion de función
def hello(name="yo"):
    print("Hello " + name + "!")

hello("joey")
hello("sus")
hello("qwerty")
hello()


def ad(n1, n2):
    return n1 + n2
print(ad(122, 666))

add = lambda n3, n4: n3 + n4

print(add(43, 34))