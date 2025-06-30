for i in range(1, 11):
    print(i)
else:
    print('Fim!')


# Aqui o eles não vai ser execultado
for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim!')
