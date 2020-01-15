def dodatek_stazowy(lata):
    if lata <= 5:
        dodatek = (lata * 100)
    elif  5<lata<=8:
        dodatek = 500 + ((lata - 5)*200)
    else:
        dodatek = 1100 + ((lata-8))*50
    
    print (dodatek)
    
lata = int(input('Wprowadź ilość lat: '))

dodatek_stazowy(lata)