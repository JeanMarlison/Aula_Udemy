#class Data:
#    pass

#vmaos fazer usando o self
class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 1
d1.mes = 7
d1.ano = 2025
print(d1)

#print(f'{d1.dia}/{d1.mes}/{d1.ano}')

d2 = Data()
d2.dia = 2
d2.mes = 7
d2.ano = 2025
print(d2)