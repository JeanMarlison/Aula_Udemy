#[expressão for intm in list if condicional]
doborsDosPares = [i * 2 for i in range(10) if i % 2 == 0]
print(doborsDosPares)


#Versão "normal"
doborsDosPares = []
for i in range(10):
    if i % 2 == 0:
        doborsDosPares.append(i * 2)
print(doborsDosPares)