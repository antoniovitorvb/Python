# listas
lista = [1,4,6,3,8,19,-5,0]
vog = ['a','e','i','o','u']

l = list("eXcript")
ll = list(["eXcript"]) # ou ll = list(("eXcript",))

a = [lista,l,vog,ll,[1,2,3]]
# print(a)
# print("a[0]: ",a[0],"a[2][2]: ",a[2][2])
# print("a[-1]: ",a[-1]) # OU a[len(a)-1]

b = [1,2,3]

c = b + [4,5,6]
c = c + [7] # OU c.append(7)

10*[1] # R: rep(1,times = 10)

for item in vog:
    print(item)

# indice = list(range(len(lista)))
# for i in indice:
#     lista[i]+=100
# print(lista)

# for i in range(len(lista)):
#     lista[i] += 100
# print(lista)

for idx, item in enumerate(lista):
    lista[idx] += 100
print(lista)