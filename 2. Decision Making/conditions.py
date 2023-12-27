# tomada de decisao

a = input("a = ")

if (a==10):
    print("Fechou!")
else:
    print("Deu ruim")

acao = input("[ y / n ]? ")

if (acao == 'y' or acao == 'Y'):
    print("executando")
elif (acao == 'n' or acao == 'N'):
    print("deixa quieto")
else:
    print("Cê é palhaço é??")

idade = input("Sua idade: ")

if(idade<0):
    print("É Benjamin Button agora é?")
elif(idade>150):
    print("Pronto! é o Raylander")
else:
    print("idade  = ", idade)