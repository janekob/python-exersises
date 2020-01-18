
    
def konwersja(cyfra):
    x=['zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']
    return x[int(cyfra)]

def slownie(liczba):
    slowo=str(liczba)
    dlugosc=len(slowo)
    zapis=''
    for x in range(0,dlugosc):
        zapis+=konwersja(slowo[x])
        if not x==dlugosc-1:
            zapis+=','
    return zapis

try:
    dane=input('Wprowadź liczbę: ')
except ValueError:
    print('Wprowadź prawidłową liczbę: ')       

print(slownie(dane))
