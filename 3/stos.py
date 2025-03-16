class Stos:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.stos = [None] * pojemnosc
        self.poczatek = 0
        self.koniec = 0
        self.ilosc = 0
    def dodaj(self,value):
        if self.ilosc == self.pojemnosc:
            print("Stos pełny")
            return
        self.stos[self.koniec] = value
        self.koniec += 1
        self.ilosc += 1
        print(f"Stos po dodaniu {value}: {self.stos}")
    def usun(self):
        if self.ilosc == 0:
            print("Stos pusty")
            return None
        item = self.stos[self.koniec-1]
        self.stos[self.koniec-1] = None
        self.koniec -= 1
        self.ilosc -= 1
        print(f"Usuniety element {item}")
        return item
    def szukaj(self,item):
        if self.ilosc == 0:
            print("Stos pusty")
            return None
        for i in range(self.iloscs):
            if self.stos[i] == item:
                return print(f"Znaleziono {item} na pozycji {i+1}")
    def wyswietl(self):
        index = 0
        while index < self.ilosc:
            print(self.stos[index], end=" ")
            index += 1
        print()
        return
stos = Stos(3)
stos.dodaj(4)
stos.dodaj(6)
stos.dodaj(8)
stos.dodaj(1)
stos.wyswietl()
stos.szukaj(4)
stos.usun()
stos.usun()
stos.dodaj(10)
stos.dodaj(21)
stos.usun()
stos.usun()
stos.usun()
stos.usun()
stos.wyswietl()




