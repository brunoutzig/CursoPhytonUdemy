#condicionais if, elif, else, reutilizei a calculadora de IMC para fazer esta aula.

entrada = input('Você deseja "entrar" ou "sair" da calculadora de IMC? ')

if entrada == 'entrar':

    nome = input('Qual seu nome? ')

    peso = input('Qual seu peso? ')

    altura = input('Qual sua altura em metros? ')
    

    alturafloat = float(altura)
    pesofloat = float(peso)

    imc = pesofloat / alturafloat ** 2
    print(f' {nome}seu IMC é de{imc:.2f}')

elif entrada == 'sair':

    print('tenha um bom dia')
else:

    print('você não digou nem "entrar" e nem "sair" ')
    
    











     