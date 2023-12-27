# Comparando caracteres:

print('De acordo com a tabela ASCII:')
print("'a' > 'x'?", 'a' > 'x')
print("'a' > 'X'?", 'a' > 'X')
print("'a' > '1'?", 'a' > '1')

## chr() retorna o caractere de um número ASCII
print('ASCII: 100 =', chr(100))
## ord() retorn o valor ASCII de um caractere
print("'d' em ASCII =", ord('d'))

for c in range(123):
    print(
        'ASCII', c,
        '=', chr(c))

# Comparando Strings