# #operadores and, or, not
# # e, ou, não
senhapermitida =  '123456'
entrada = input( '[E]Entrar [S]Sair ' )
senha = input( 'Senha: ')
if (entrada ==  'E' or entrada == 'e') and senha == senhapermitida:
     print("Você entrou no software")

else:
    print("Você saiu do software")


print(True and True and False and True) # Teste do curto circuito
senha1 = input('Senha') or'Sem senha'
print(senha1)

print(not True)#not serve para inverter expressões
print(not False) #not serve para inverter expressões

nome =input('digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
print(nome[2])
print('o' in nome)# verifica se a letra existe no nome
print('B'  not in nome)

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não està em {nome}')

