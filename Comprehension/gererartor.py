# O gererartor Gera os dados por demanda, ou seja só gera quando for solicitado.


gererartor = (i ** 2 for i in range(10) if i % 2 == 0)
prit(next(gererartor)) # Saída 0
prit(next(gererartor)) # Saída 4
prit(next(gererartor)) # Saída 16
prit(next(gererartor)) # Saída 36
prit(next(gererartor)) # Saída 64
prit(next(gererartor)) # Erro

