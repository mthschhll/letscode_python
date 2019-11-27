#exercicio 6
n1 = float(input('digite nota prova 1:'))
n2 = float(input('digite nota prova 2:'))
n3 = float(input('digite nota prova 3:'))
media = (n1 + n2 + n3)/3
if(media) >= 6:
    print('{:.1f}'.format(media),'passou')
if(media) < 6:
    print('{:.1f}'.format(media), 'reprovou')