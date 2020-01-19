def bez_duplikatow(tablica):  
    zbior = set()
    zbior_prim=set()
    for x in tablica:
        if x not in zbior and x not in zbior_prim:
            zbior.add(x)
        else:
            zbior_prim.add(x)
            zbior.remove(x)
    return zbior

try: 
    tablica = [] 
      
    while True: 
        tablica.append(int(input('Wprowadź liczbę naturalną lub znak by otrzymać wynik: '))) 
except:
    print(bez_duplikatow(tablica))