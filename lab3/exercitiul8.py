import datetime
data_input = "2023-04-24 09:03:32"
extrage_anul = lambda s: s[:4]
extrage_luna = lambda s: s[5:7]
extrage_ziua = lambda s: s[8:10]
extrage_ora = lambda s: s[11:19]
print(extrage_anul(data_input))
print(extrage_luna(data_input))
print(extrage_ziua(data_input))
print(extrage_ora(data_input))