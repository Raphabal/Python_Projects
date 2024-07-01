#Conversão de reais para dolar e euro
real = float(input('informe quanto tem de dinheiro em carteira em R$ Reais: '))

#Cotação atual
dolar = real/5.27
euro = real/5.37

#Mostra conversão das moedas
print('Com R${} voce pode comprar USD${:.2f} Dolares!'.format(real, dolar))
print('Com R${} voce pode comprar EU${:.2f} Euros!'.format(real, euro))
