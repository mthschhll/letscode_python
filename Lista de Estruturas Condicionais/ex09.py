#exercicio 9
#preco antigo
pa = float(input('digite o valor de acordo com o preço antigo: R$'))
p1 = 0.05
p2 = 0.10
p3 = 0.13
p4 = 0.15

if(pa) <= 50:
    valor_novo = p1 * pa + pa
elif(pa) <= 100:
    valor_novo = p2 * pa + pa
elif (pa) <= 150:
    valor_novo = p3 * pa + pa
else:
    valor_novo = p4 * pa + pa

if(valor_novo) <= 80:
    print('barato')
elif(valor_novo) <= 115:
    print('razoavel')
elif(valor_novo) <= 150:
    print('normal')
elif(valor_novo) <= 170:
    print('caro')
else:
    print('muito caro')