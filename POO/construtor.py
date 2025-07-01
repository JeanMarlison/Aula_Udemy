class Data:
    #Aqui vmaos fazer o construtor:
    def __init__(self, dia, mes, ano):
        # Em python não posso ter mias de um construtor, porém podemos ter parârametro opcionais:
#   def __init__(self, dia = 1, mes = 7, ano = 2025):    
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(1, 7, 2025) 
#d1.dia = 1
#d1.mes = 7
#d1.ano = 2025
print(d1)

d2 = Data(5, 12, 2019)
#d2.dia = 2
#d2.mes = 7
#d2.ano = 2025
print(d2)