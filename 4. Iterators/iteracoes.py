x = 0
while(x<=10):
    print(x)
    x += 1
else:
    print("else")
    x = 0

for s in "eXcript":
    print(s)

range(0,10,2)
list(range(0,10,2)) # range([comeco], final[, passo)

list(range(10,0,-1)) # Decrescente

for i in range(10,0,-1):
    print(i)

print("Antes de entrar no laco:")
for i in range(10):
    print(i)
    if(i==5):
        break
    print("continue")
print("depois de entrar no laco")

print()
print("inicio")
i = 0
while(i<10):
    i+=1
    if(i%2==0):
        continue # interrompe esse ciclo e pula pro proximo
    print(i)
    
    if(i>=7):
        break # para todo o laco
else:
    print("else")
print("fim")
print()