horario = input('Favor informar o horario: ')
horarioint = int(horario)

if horarioint >= 0 and horarioint <= 11:
    print('Bom dia')

elif horarioint >= 12 and horarioint <= 17:
    print('Boa tarde')

elif horarioint >= 18 and horarioint <= 23:
    print('Boa noite')

else:
    print("não conheço essa hora")

