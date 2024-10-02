# lista_amigo=["abel","anthony","edith","ruth"]
# diccionario={amigo:len(amigo) for amigo in lista_amigo}
# print(diccionario)
for lista_numeros in range(1,100):
    lista_nueva=[int(n) for n in lista_numeros.split(",") if int (n)%2==0]
    print(lista_nueva)