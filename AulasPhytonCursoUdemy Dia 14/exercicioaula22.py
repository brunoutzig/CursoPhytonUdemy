nome = input( 'Digite seu nome: ')
idade = input( 'Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    nomeinvertido = nome
    print(f'Seu nome invertido é {nomeinvertido[::-1]}')

else:
    
    print("Parece que você deixou campos vazios")

encontrar = input('Digite o caractere que deseja encontrar: ')


if encontrar in nome: 
     print('O caractere desejado se encontra no seu nome')

else:
     print('O caractere desejado não está presente no seu nome')


     print(f'Seu nome tem {len(nome)} letras')
     print(f'A primeira letra do seu nome é: {nome[0]}')
     print(f'A última letra do seu nome é: {nome[-1]}')



