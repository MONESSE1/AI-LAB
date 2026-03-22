import time

tari_risc = ["coreea de nord", "siria", "iran"]
tranzactii_suspecte = 0
timpi_tranzactii = []

print("Procesam tranzactiile...\n")

while tranzactii_suspecte < 3:
    try:
        suma = float(input("Introdu suma (RON): "))
    except ValueError:
        print("Sumă invalida. ")
        continue

    tara = input("Introdu tara: ").strip()

    acum = time.time()
    timpi_tranzactii = [t for t in timpi_tranzactii if acum - t <= 60]
    timpi_tranzactii.append(acum)

    este_suspecta = False
    status = "Sigura"
    motiv = ""

    if tara.lower() in tari_risc:
        status = "Frauda"
        motiv = "(tara cu risc ridicat)"
        este_suspecta = True
    elif suma > 10000:
        status = "Suspicioasa"
        motiv = "(suma mare)"
        este_suspecta = True
    elif len(timpi_tranzactii) > 3:
        status = "Suspicioasa"
        motiv = "(posibil bot activity)"
        este_suspecta = True

    if este_suspecta:
        tranzactii_suspecte += 1
        print(f"Tranzactie: {suma} RON din {tara} → {status} {motiv}\n")
    else:
        print(f"Tranzactie: {suma} RON din {tara} → Sigura\n")

print("3 tranzactii suspecte detectate! Cont blocat.")