def suma_liczb(a,b,c,d):
    suma = 0
    while a <=b:
        if a % c == 0 or a % d == 0:
            suma += a
            a += 1
        else:
            a+=1
    print(suma)
    
a=int(input('podaj dolną granicę przedziału: '))
b=int(input('podaj górną granicę przedziału: '))
c=int(input('podaj pierwszy dzielnik: '))
d=int(input('podaj drugi dzielnik: '))

suma_liczb(a,b,c,d)    