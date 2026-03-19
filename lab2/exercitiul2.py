nota =int (input("introdu o nota="))

nota_valide = list(range(1,11))

print(nota_valide)

while nota not in nota_valide:
    nota =int (input("reintrodu o nota="))

if nota > 5:
    print("reexaminare")

elif nota >= 6:
        print("suficient")

elif nota >= 8:
        print("bine")

else nota >= 10:
        print("excelent")

