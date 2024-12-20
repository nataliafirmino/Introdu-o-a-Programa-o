horas=int(input('Digite as horas:'))
minutos=int(input('Digite os minutos :'))
segundos=int(input('Digite os segundos:'))
total_segundos=horas*3600+minutos*60+segundos
total_segundos_dia=24*3600
segundos_restantes=total_segundos_dia-total_segundos
#Exibe o resultado
print('Faltam', segundos_restantes, 'segundos até o final do dia.')