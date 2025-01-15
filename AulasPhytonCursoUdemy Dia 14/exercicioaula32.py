nome = 'Bruno'

i = 0 
n_nome = ''
while  i < len(nome):
    letra = nome[i]
    n_nome += f'*{letra}'
    i += 1

    print(n_nome)