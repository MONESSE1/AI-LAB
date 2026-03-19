import random

print("Bun venit la Loterie")

numere =random.sample(range(1,49), 6)
numere_bilet =[]

contor = 1

while True:
    ghicire = int(input(f"Alege numărul {contor}: "))
    if ghicire < 1 or ghicire > 49:
        print("  -> Eroare: Numărul trebuie să fie între 1 și 49!")

    elif ghicire in numere_bilet:
        print("  -> Eroare: Ai ales deja acest număr! Alege altul.")

    else:

        numere_bilet.append(ghicire)
        if contor == 6:
            break

        contor += 1



print("\n--- Extragere Finalizată ---")
print(f"Numerele alese de tine: {numere_bilet}")
print(f"Numerele câștigătoare:  {numere}")
