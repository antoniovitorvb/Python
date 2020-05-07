# Operadores logicos

b = not True
y = 2
b = ((y == 0) == False)
if (b):
    print("O valor da variável b é True")
else:
    print("O valor da variável b é False")

a = float(input("a = "))
b = float(input("b = "))

print("a == b: ", a==b) #equal
print("a != b: ", a!=b) #not equal

print("a >= b: ", a>=b) #equal or greater than
print("a <= b: ", a<=b) #equal or less than

# Operadores logicos 2

cond1 = (a==b) and not(a!=b)
cond2 = (a > b) or (a==b)

vet = (1,2,3,4,5)
print(type(vet))

cond3 = (a > 2) or (a in vet)
cond4 = cond1 or cond2

print("Cond1: ", cond1)
print("Cond2: ", cond2)
print("Cond3: ", cond3)
print("Cond4: ", cond4)