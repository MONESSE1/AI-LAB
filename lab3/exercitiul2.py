def genereaza_factura(nume_client, **produse):
    print(f"Factura: {nume_client}")
    print("-" * 30)

    total = 0
    for produs, pret in produse.items():
        print(f"{produs}: {pret} RON")
        total += pret

    print("-" * 30)
    print(f"Total: {total} RON")



genereaza_factura("Eduard Mihai", Paine=3.5, Lapte=7, Cafea=105)