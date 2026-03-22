import time

inv = []
print("Alege direcția: 1 (Stânga) 2 (Dreapta)")
alegere = input("Rspuns: ")

if alegere == "1":
    print("Ai plecat in calatorie")
    time.sleep(1)

    print("Pare ca ai gasit o caruta rasturnata")
    time.sleep(1)

    print("Ai gasit o comoara!")
    inv.append("Comoara")

elif alegere == "2":
    print("Ai plecat in calatorie")
    time.sleep(1)

    print("Ai dat de un lup.")
    time.sleep(1)

    print("Ai vrut sa il ataci dar ai fost omorat!")
else:
    print("Alegere invalidă.")

print(f"Final. Ai în inventar: {inv}")