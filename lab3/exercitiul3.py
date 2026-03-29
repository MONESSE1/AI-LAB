def normalizare(lista_numere):

    minim = min(lista_numere)
    maxim = max(lista_numere)
    interval = maxim - minim
    if interval == 0:
        return [0.0 for x in lista_numere]


    return [(x - minim) / interval for x in lista_numere]

date = [10, 20, 30, 40, 50]
normalizare = normalizare(date)

print(f"Date originale: {date}")
print(f"Date normalizate: {normalizare}")