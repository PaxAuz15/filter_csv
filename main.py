import csv

reader = csv.reader(open(r"intest.csv"),delimiter=';')
cartera = input('Escriba una cartera: ')

filtered = filter(lambda p: cartera == p[0], reader)
# print(filtered)

csv.writer(open(r"output.csv",'w'),delimiter=';').writerows(filtered)

readerToSum = csv.reader(open("output.csv"), delimiter=';')

sumaTotal = 0
for row in readerToSum:
    _sumaTotal = row[2]
    try:
        _sumaTotal = float(_sumaTotal)
    except ValueError:
        _sumaTotal = 0
    
    sumaTotal += _sumaTotal

print(f"Suma total de la cartera {cartera} es {sumaTotal}")