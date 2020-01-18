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

tablica = list(input('Wprowadź liczby naturalne: '))

bez_duplikatow(tablica)