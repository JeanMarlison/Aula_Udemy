def todosParametros(*args, **kwargs):
    print(f'args: {args}')
    print(f'Kwargs: {kwargs}')

if __name__=='__main__':
    todosParametros('Para','A','Tupla')
    todosParametros(Dicioanrio='Para',Muitas='Opções')
    todosParametros()
    todosParametros('Aqui','Vamos','Mandar','Tudo', junto='E', mesturado='De uma vez')