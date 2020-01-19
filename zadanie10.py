def ile_liter(litera):
    if len(litera) != 1:
        print('Blad danych wejsciowych! Dlugosc szukanej frazy: ' + str(len(litera)) )
        return ile_liter(input('Wprowadź szukana litere: '))

    lista_slow = []
    with open("./dane.txt", "r") as f:
        for line in f:
            lista_slow.extend(line.split())

    slowa_w_zakresie = [item for item in lista_slow if 3 <= len(item) <= 5]
    licznik =0
    for slowo in slowa_w_zakresie:
        if slowo.find(litera)!=-1:
            licznik+=1
    print (licznik)
ile_liter(input('Wprowadź szukana litere: '))