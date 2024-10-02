# #crear una lista  de numeroa enteros del siguiente texto
# texto="1,4,8,9,6"
# nueva_lista=[]
# for n in texto.split(","):
#     nueva_lista.append(int(n))
# print(nueva_lista)
#aplicando la tecnica vlc valor bucle y concion
#  texto="1,4,8,9,6"
# # nueva_lista=[int(n) for n in texto.split(",") if int (n)%2==0]
# # print(nueva_lista)
#diccionario por comprencion 
nueva_amigos=["abel","anthony","edith","ruth"]
diccionario={}
for _,v in enumerate(nueva_amigos):
    diccionario[v]=len(v)
print(diccionario) 
#aplicando el vlc 
lista_amigo=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigo) for amigo in lista_amigo}
print(diccionario)