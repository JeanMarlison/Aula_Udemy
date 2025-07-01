# def fatorial(n):
#     return n * (fatorial(n - 1)) if (n - 1) > 1 else 1

# if __name__=='__main__':
#     print(f'10! = {fatorial(10)}')




#Quando o número inserido para fazer o fatorial for menor que 1, a função irá retornar 1 como resultado automaticamente.
def fatorial(n):

    return (n * fatorial(n-1)) if n > 1 else 1

if __name__ == "__main__":

    n = 0

    print(f'{n}! = {fatorial(n)}')