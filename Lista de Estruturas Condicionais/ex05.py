#exercicio 5
#a)
i = int(input('digite sua idade:'))
if(i)>=151:
    print('erro')
elif(i)<=-1:
    print('erro')
else:
    print('ok')
#b)
s = float(input('digite seu salario:'))
if(s) < 0:
    print('erro')
else:
    print('ok')
#c)
sx = str(input('digite seu sexo (m),(f),(outro):'))
if(sx) == ('m'):
    print('ok')
if(sx) == ('f'):
    print('ok')
elif(sx) == ('outro'):
    print('ok')    
else:
    print('erro')