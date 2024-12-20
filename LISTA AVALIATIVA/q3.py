
trem1=0
trem2=40000
tempo=0

while True:
    tempo+=1
    trem1+=30
    trem2-=40
    if  trem1>trem2:
        break
   
print(f'Serão necessários {tempo} segundos para os maquinistas pararem as locomotivas.')