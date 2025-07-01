# Callable Posso passar uma função para uma função e diferentes parametros para um função.
#!/usr/local/bin/python3
class Potencia:
    # Calcula uma pontência específica

    #Sempre o 1° parâmentro vai ser SELF, pode usar outro nomes, mas o 1° parârametro representa a instância atual.
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente
    


if __name__=='__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)