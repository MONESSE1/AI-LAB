comentariu = input("Comentariu: ").lower().split()

pozitiv = ["bine","bravo","super"]
negativ = ["naspa","prost","groaznic"]

if any(cuvant in comentariu for cuvant in pozitiv):
    print("Comentariu pozitiv")
elif any(cuvant in comentariu for cuvant in negativ):
    print("Comentariu negativ")
else:
        print("Comentariu normal")