def dodatek_stazowy(wprowadzoneLata):
    try:
        lata = int(wprowadzoneLata)
    except ValueError:
        print('Blad danych wejsciowych! Wprowadzone lata nie sa liczba')
        return dodatek_stazowy(input('Wprowadź liczbe lat: '))
    if lata < 0:
        print('Blad danych wejsciowych! Wprowadzona liczba mniejsza niz zero...' )
        return dodatek_stazowy(input('Wprowadź liczbe lat: '))
    elif 0 <= lata <= 5:
        dodatek = (lata * 100)
    elif  5 < lata <= 8:
        dodatek = 500 + ((lata - 5)*200)
    else:
        dodatek = 1100 + ((lata-8))*50
    
    print (dodatek)
    
dodatek_stazowy(input('Wprowadź liczbe lat: '))