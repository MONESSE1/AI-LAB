preturi_brute = [100, None, 50, 200, None, 30]

fara_none = filter(lambda x: x is not None, preturi_brute)
preturi_reduse = list(map(lambda x: x * 0.9, fara_none))

print(f"Prețuri finale: {preturi_reduse}")
