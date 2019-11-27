#exercicio 8
x = 0
nao = (x)
q1 = (str(input('''Responda as questoes a baixo com "sim" ou "nao" 
Telefonou para a vítima?''')))
q2 = (str(input('Esteve no local do crime?')))
q3 = (str(input('Mora perto da vítima?')))
q4 = (str(input('Devia para a vítima?')))
q5 = (str(input('Já trabalhou com a vítima?')))
if q1 == ('sim'):
    x = (x + 1)
if q2 == ('sim'):
    x = (x +1)
if q3 == ('sim'):
    x = (x + 1)
if q4 == ('sim'):
    x = (x + 1)
if q5 == ('sim'):
    x = (x + 1)
print(x)
if x == 5:
    print('assassino')
if x == 4:
    print('cumplice')
if x == 3:
    print('cumplice')
if x == 2:
    print('suspeito')
if x == 1:
    print('liberado')
if x == 0:
    print('liberado')