import random

def quebraSenha(num):
    try:
        senha = num

        senha = list(str(senha))

        quebraSenha = [random.randint(0,9) for num in range(0,len(senha))]

        contador = 0
        listaSenha = [int(num) for num in senha]
        while listaSenha != quebraSenha:
            contador += 1
            quebraSenha = [random.randint(0, 9) for num in range(0, len(senha))]
            print(quebraSenha)
        else:
            print(f'A senha digitada é {quebraSenha}\nForam {contador} tentativas')
    except Exception as e:
        print('Digite somente numeros')

if __name__ == '__main__':
    quebraSenha(1)