# Fatiando (Slicing) listas

frase = "Bem-vindo ao curso de Python" 
print(frase[:10]) # lista[comeco = 0 : final : passo = 1]
print(frase[10::2])

# Anexando
l = ['a','b','c']
l = l + ['d']
l.append('e') # sempre na ultima posicao
print(l)

# Inserindo
ll = l # list aliasing
ll.insert(1,'aa') # (index, elemento)
print(ll)

# limpar por completo
lc = ll[:] # list clone
print("antes: ",lc)
lc.clear()
print("depois: ",lc)

# deletar um item
ll.pop() # retorna o ultimo elemento excluido
ll.pop(1) # exclui elemento de index 1
print(ll)

del(ll[1:3]) # lista[[comeco]: final[ : passo = 1]
l = list(range(1,11))
del(l[::2])
print(ll)
print(l)

# ordenando
n = [20, -5, 3, 7, 102, 27, -27, 8, 0, 10]
nd=n[:]
print(n)
n.reverse() # inverte a ordem dos elementos
print(n)

n.sort() # crescente
print("cres.: ", n)

# nd.sort(); nd.reverse() # Descrescente
nd.sort(reverse=True)
print("decr.: ", nd)

# quantidade de elementos
l = ['a','b','c','d','e',]
l.insert(3,'a')
l.append('a')
l.count('a') # quantas vezes 'a' aparece na lista
l.index('b') # retorna qual o index de 'b' ou primeira ocorrencia