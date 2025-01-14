#introdução as f-strings

nome =  'Bruno'
altura = 1.83
peso = 68
imc = peso / altura ** 2 

#print( ' Seu nome ê', nome)

#print( ' Sua altura ê', altura)

#print( ' Seu peso ê', peso)

#print( ' portanto seu imc ê de', imc)

linha1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu imc ê de'
linha2 = f'{imc:.2f}'
print(linha1)
print(linha2)




