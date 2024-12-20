gasolina=float(input('Digite o preço da gasolina:'))
alcool=float(input('Digite o preço do álcool:'))
if  alcool <70/100*gasolina:
    print('o álcool é mais vantajoso que a gasolina')
else:
    alcool>70/100*gasolina
    print('A gasolina é mais vantajosa que o álcool')