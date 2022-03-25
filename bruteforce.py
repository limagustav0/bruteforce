import random

def quebraSenha(num):
    try:
        #Transforma a senha numérica digitada numa lista de string
        senha = list(str(num))

        #Cria uma sequência de numeros aleatórios de acordo com a quantidade de senhas digitadas acima
        quebraSenha = [random.randint(0,9) for num in range(0,len(senha))]

        #Contador para somar o tanto de tentativas
        contador = 0

        #Transforma a senha digitada numa lista de dados do tipo INT
        listaSenha = [int(num) for num in senha]

        #Loop while para encontrar a senha digitada
        while listaSenha != quebraSenha:
            contador += 1
            #Quando a senha contida na listaSenha não é encontrado pelo quebraSenha, o conjunto de dados é aleatóriamente redefinido
            quebraSenha = [random.randint(0, 9) for num in range(0, len(senha))]
            print(quebraSenha)
        else:
            print(f'A senha digitada é {quebraSenha}\nForam {contador} tentativas')
    except Exception as e:
        print('Digite somente numeros')

if __name__ == '__main__':
    quebraSenha(12345)
