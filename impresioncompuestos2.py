#importa el paquete 'string' 
import string
import re

#Abre el archivo y lo lee para poder elaborar la limpieza
archivo=input()
f=open(archivo)
contenido= f.read()
f.close()
#f=open("Morfolex1.txt")
#contenido= f.read()
#f.close()

#Define los elementos que serán eliminados
conjunto=string.punctuation
conjunto2=['...','”','“','¿','?','-','""']

#Define el conjunto de elemntos que serán sustituidos y el caracter ''
for char in contenido:
    if char in conjunto:
        contenido=contenido.replace(char,'')

for char in contenido:
    if char in conjunto2:
        contenido=contenido.replace(char,'')

#Pasa todos los caracteres a minúsculas
    contenido=contenido.lower()

##print(contenido)

#Elabora una lista de las palabras que se encuentran entre espacios en blanco
lista=contenido.split()

#Imprime el total de palabras
#print('palabras despues de la limpieza:')
#print(len(lista))

#Define la lista vacía donde se incorporarán las palabras >=7
lista2=[]
#Descarta todos los elementos con condición anterior
for i in lista:
    if len(i)>=8:
        #print(i)
        lista2.append(i)
#print(lista2)

#Imprime el total de elementos con la condición >=7
#print('palabras despues de la condición >=7:')
#print(len(lista2))

#Abrir la lista de verbos basada en el corpus Morfolex
f2=open("Lista.txt")
g=f2.read()
#print(g)
#print('Numero de verbos extraidos de la base morfolex')
verbos=g.split()
#print(verbos)
print(len(verbos))

lista3=[]

for q in lista2:
    if 'ción' in q:
        lista3.append(q)
        #print(q)
#print('palabras deverbales con ción:')
#print(len(lista3))

lista4=[]
for q in lista2:
    if 'miento' in q:
        lista4.append(q)
        #print(q)
#print('palabras deverbales con miento:')
#print(len(lista4))

lista5=[]
for q in lista2:
    if 'mente' in q:
        lista5.append(q)
        #print(q)
#print('palabras deverbales con mente:')
#print(len(lista5))

lista6=[]
for q in lista2:
    if 'dor' in q:
        lista6.append(q)
        #print(q)
#print('palabras deverbales con dor:')
#print(len(lista6))
#Agrupa las sublistas de deverbales para posterioemente borrarlas

lista8=[]
for q in lista2:
    if 'icio' in q:
        lista8.append(q)

lista10=[]
for q in lista2:
    if 'arle' in q:
        lista10.append(q)

lista11=[]
for q in lista2:
    if 'erle' in q:
        lista11.append(q)

lista12=[]
for q in lista2:
    if 'erlo' in q:
        lista12.append(q)

lista13=[]
for q in lista2:
    if 'arlo' in q:
        lista13.append(q)

lista14=[]
for q in lista2:
    if 'aban' in q:
        lista14.append(q)

lista15=[]
for q in lista2:
    if 'aron' in q:
        lista15.append(q)

lista16=[]
for q in lista2:
    if 'ero' in q:
        lista16.append(q)

lista17=[]
for q in lista2:
    if 'ario' in q:
        lista17.append(q)

lista18=[]
for q in lista2:
    if 'ará' in q:
        lista18.append(q)

lista19=[]
for q in lista2:
    if 'erá' in q:
        lista19.append(q)


       
lista7=lista3[:]+lista4[:]+lista5[:]+lista6[:]+lista8[:]+lista10[:]+lista11[:]+lista12[:]+lista13[:]+lista14[:]+lista15[:]+lista16[:]+lista17[:]+lista18[:]+lista19[:]
#print(lista7)
#print('Total de palabras deverbales')
#print(len(lista7))

#Sustrae la lista7 de la lista2 y la manada a una nueva lista
def set_approach(lista2,lista7):
    return list(set(lista2)-set(lista7))
sd=list(set(lista2)-set(lista7))

#print(list(set(lista2)-set(lista7)))
#print('Elementos despues de eliminar los deverbales')
#print(len(sd))

#match=[]
#for x in sd:
    #if x in sd:
        #match.append(x)
        #print(sd)

#t=list(set(sd)&set(verbos))
#print(t)

#Solo me devuelve un conjunto vacío pues solo compara elementos identicos y no parciales
#Eliminar todos los deverbales de las listas 3, 4, 5 de la lista 2??

#Inicia el match de lista de verbos con el corpues que ya cumplió las condiciones previas
#cómo vuelvo temp una lista?# Este simple ejemplo se hace con regex
print('Lista de verbos y compuestos con los que coinciden')
for list in verbos:
    for tem in sd:
        if re.match(list, tem, re.I):
            print(list,tem)
            
            



