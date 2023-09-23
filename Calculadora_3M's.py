from collections import Counter
def moda (n):
    frequencias = {}


    for elemento in n:
        if elemento in frequencias:
            frequencias[elemento] += 1
        else:
            frequencias[elemento] = 1


    moda = []
    max_frequencia = max(frequencias.values())

    for elemento, frequencia in frequencias.items():
        if frequencia == max_frequencia:
            moda.append(elemento)


    print("A(s) moda(s) é(são):")
    for valor in moda:
        print(f" - {valor}, que se repete {max_frequencia} vez(es) na lista.")       
numeros=[]
while True:
    numeros.append(float(input(' insira os numeros da lista:')))
    conf=input('deseja adicionar outro numero [S] ou [N] ?').upper()
    if conf == 'S':
        continue
    if conf =='N':
        break
numbers= len(numeros)
media = sum(numeros)/numbers
numeros_ordenados=sorted(numeros)
numero_mediana= numbers/2 
if numbers %2 == 0 :
    while numero_mediana:
        numero_mediana = int(numero_mediana)
        break
    n_m = numeros_ordenados[numero_mediana], numeros_ordenados[numero_mediana+1]
    mediana= sum(n_m)/2
else :
    numero_mediana+=0.5
    while numero_mediana:
        numero_mediana = int(numero_mediana)
        break
    mediana=numeros_ordenados[numero_mediana]

#desvio = valor menos a média 
desvios=[]
desvios_ao_2=[]
for valores in numeros :
    desvio=valores-media
    desvios.append(desvio)
    desvio_ao_2=(valores-media)**2
    desvios_ao_2.append(desvio_ao_2)

#varianca 
#media dos desvios ao quadrado
variancia= sum(desvios_ao_2)/len(desvios_ao_2)


#desvio padrao
#raiz quadrada da variança
desvio_padrao= variancia**(1/2)

#coeficiente variação
#(desvio padrao/ media )*100
cv=(desvio_padrao/media)

print(f' A media dessa lista é {media}')
print(f' A mediana dessa lista é {mediana}')
moda(numeros)
print(' Os desvios são : ')
for x in desvios:
    print(f' {x:.2f} ')
print(f'A Variança é {variancia:.2f} ')
print(f'O Desvio Padrão é {desvio_padrao:.2f}')
print(f'O Coeficiente de Variação é {cv:.2%}')




