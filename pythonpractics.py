numbers=[1,2,34,5]

delta=list(map(lambda x: x**2 ,numbers))

print(delta)

lata=lambda x:x+3

print(lata(4))

print(lata(7))

nombre={
    "place":"new york",
    "month":"january",
    "name":"juan"
    
    
}

print(nombre["place"])

for key, values in nombre.items():
    print(nombre[key])
    
print(nombre["month"])


def puto(x,y):
    return x,y

defe, fer=puto(2,4)

print(defe)
print(fer)

print(puto(3,5))