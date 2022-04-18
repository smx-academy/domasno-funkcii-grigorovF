
from re import I


class Prodavnica:
    def __init__(self):
        self.imeProizvodi = []
        self.cena = []
        self.kolicina = []
        self.kupiProizvod = []
        self.kupiKolicina = []

    def dodajProizod(self, novProizvod):
        self.imeProizvodi.append(novProizvod)

    def dodajCena(self, cena):
        self.cena.append(cena)
    
    def dodajKolicina(self, kolicina):
        self.kolicina.append(kolicina)

    def dodajKupiProizvod(self, proizvod):
        self.kupiProizvod.append(proizvod)
    def dodajKupiKolicina(self, kolicina):
        self.kupiKolicina.append(kolicina)

    def smetka (self):
        n = len(self.imeProizvodi)
        m = len(self.kupiProizvod)
        s = 0
        for i in range(0,n):
            for j in range(0,m):
                if (self.imeProizvodi[i] == self.kupiProizvod[j]):
                    print("{} \t {} \t {}".format(self.imeProizvodi[i], self.kupiKolicina[j], self.kupiKolicina[j]*self.cena[i]))
                    s = s + self.kupiKolicina[j]*self.cena[i]
        print("Vkupno za plakanje: ", s)

    def magacin (self):
        n = len(self.imeProizvodi)
        m = len(self.kupiProizvod)

        for i in range(0,n):
            for j in range(0,m):
                if (self.imeProizvodi[i] == self.kupiProizvod[j]):
                    self.kolicina[i] = self.kolicina[i] - self.kupiKolicina[j]

        for i in range(0,n):
            print(self.imeProizvodi[i] + " " + self.kolicina[i] + " " + self.cena[i]) 


print ("Polnenje Magacin: ")
p = Prodavnica()
while True:
    p.dodajProizod(input("Vnesi proizvod: "))
    p.dodajCena(int(input("Vnesi cena: ")))
    p.dodajKolicina(int(input("Vnesi kolicina: ")))
    c = input("Nov Proizvod?\n")
    if c=="da" or c=="DA" or c=="Da" or c=="dA":
        continue
    else:
        break



print("\nKupi: ")
while True:
    proizvod = input("Vnesi proizvod: ")
    kolicina = int(input("Vnesi kolicina: "))
    p.dodajKupiProizvod(proizvod)
    p.dodajKupiKolicina(kolicina)
    c = input("Nov Proizvod?\n")
    if c=="da" or c=="DA" or c=="Da" or c=="dA":
        continue
    else:
        break
print ("FISKALNA")
p.smetka()

print("Ostatok vo Magacin: ")
p.magacin()