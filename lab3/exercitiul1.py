def joaca():
    while True:
        print("\nIncepe jocul")

        p1 = input("Jucător 1 (piatra/foarfeca/hartia): ").lower()
        p2 = input("Jucător 2 (piatra/foarfeca/hartia): ").lower()


        if p1 == p2:
            print("Egalitate!")
        elif (p1 == 'piatra' and p2 == 'foarfeca') or \
             (p1 == 'foarfeca' and p2 == 'hartia') or \
             (p1 == 'hartia' and p2 == 'piatra'):
            print("Jucator 1 a castigat")
        else:
            print("Jucator 2 a castigat")


        releu = input("Rejucati? (da/nu): ").lower()
        if releu != 'da':
            print("GG")
            break

joaca()