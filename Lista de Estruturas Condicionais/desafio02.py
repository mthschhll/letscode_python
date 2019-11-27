numero_1 = float(input('Primeiro número'))
numero_2 = float(input('Segundo Número'))
numero_3 = float(input('Terceiro número'))
numero_4 = float(input('Quarto número'))

if numero_1 > numero_2:
    maior = numero_1
else:
    maior = numero_2

if numero_3 > maior:
    maior = numero_3
    
if numero_4 > maior:
    maior = numero_4

print('o maior número é',maior)