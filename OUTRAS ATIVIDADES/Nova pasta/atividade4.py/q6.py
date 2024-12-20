maca=int(input('Informe quantas maçãs foram compradas:'))
if  maca < 12:
    maca=(maca * 0.30)
else:
    maca >= 12
    maca=maca * 0.25
print('Vaor total: R$', maca)