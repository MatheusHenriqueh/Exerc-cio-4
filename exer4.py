#Exercício do curso de python

nome = input("Digite seu nome:")
idade = input('Digite sua idade:')
letra1 = nome[0]
letra2 = nome[-1]
if nome and idade:
    print(f'Seu nome é {nome}')
    print("Seu nome invertido é",nome[::-1])
    if ' ' in nome:
        print("Seu nome tem espaços")
    else:
        print('Seu nome não tem espaços')
    print('Seu nome tem',(len(nome)),'letras')
    print(f'A primeira letra do seu nome é {letra1}')
    print(f'Sua ultima letra do seu nome é {letra2}')
else:
    print("Poxa, digite algo!")