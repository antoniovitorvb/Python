s = 'Para Python, toda string é uma lista imutável'
print(s)
print(type(s))

print(
    's[0] =', s[0],
    '\ns[-1] =', s[-1]
)

# lista[x:y:z] -> x = start; y = stop; z = step
print(
    'os primeiros 5 caracteres =', s[:4],
    '\nos últimos 5 caracteres =', s[-5:],
    '\nDo 5º ao 20º =', s[4:19],
    '\ndo 10º até o final =', s[9:],
    '\nlendo a string de trás para frente =', s[::-1],
    '\nlendo tudo de 2 em 2 caracteres =', s[::2]
)