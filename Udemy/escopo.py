a = 1
b = 2

def soma(x, y):
    s = x + y
    return s

def imprime(vezes):
    for i in range(vezes):
        print(i)

print(soma(a,b))
print("")
imprime(5)

# Incrementacoes

a += b # a = a + b
a -= b # a = a - b
a *= b # a = a * b
a /= b # a = a / b
a %= b # a = a % b

aux = a; a = b; b = aux # como em C, JS, R...
# OU
a, b = b, a

# atribuicao multipla

a, b, c = 2, 4, 8

# exemplo
a, b, c = 2*a, a+b+c, a*b*c # obs: as operacoes serao feitas em paralelo

# atribuicao condicional

texto = "sim" if a==b else "nao"

# exemplo
x = int(input("x = "))
s = "par" if x % 2 == 0 else "ímpar"
print("%d é %s" %(x, s))