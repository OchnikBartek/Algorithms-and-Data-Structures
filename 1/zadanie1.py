def najwieksza(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista[len(lista)-1]


ciag = input("Podaj ciag liczb, rozdzielonych srednikami, z ktorych chcesz sprawdzic ktora jest najwieksza: ")
lista = ciag.split(';')
lista = [float(x) for x in lista]
print(f"Najwieksza liczba ze zbioru {lista} to {najwieksza(lista)}")
