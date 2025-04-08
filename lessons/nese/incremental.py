class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus

class Arstid:
    def __init__(self, nimi, eriala):
        self.nimi = nimi
        self.eriala = eriala
        self.regAeg = ""

class Haigla:
    def __init__(self):
        self.patsiendiList = []
        self.ArstidList = []
    def patsiendideKuuvamine(self):
        for index, elem in enumerate(self.patsiendiList):
            print("id:", index + 1, "Nimi:", elem.nimi, "Vanus:", elem.vanus)

    def arstideKuuvamine(self):
        for index, elem in enumerate(self.ArstidList):
            print("Id:", index + 1, "Nimi:", elem.nimi, "Eriala:", elem.eriala)


    def kohtumineTegimine(self):
        patsientiNimi = input("Sisesta patsiendiNimi: ")
        arstiNimi = input("Sisesta arstiNimi: ")
        
        
        for elem in range(self.ArstidList):
            if elem.nimi == patsientiNimi:
                patsiendiIndex = self.patsiendiList.index(elem)
            
            
    

Patsient1 = Patsient("Vsevolod", 123)
Patsient2 = Patsient("Gleb", 10)
Patsient3 = Patsient("Martin", 0)
Patsient4 = Patsient("Mama gleba (Marand)", 666)



Arstid1 = Arstid("Vsevolod", "newsmaker", ["10:00", "20:00", "11:00"])
Arstid2 = Arstid("Bogdan", "Офтальмолог", ["15:00", "17:00"])

haigla = Haigla()
haigla.patsiendiList.append(Patsient1)
haigla.patsiendiList.append(Patsient2)
haigla.patsiendiList.append(Patsient3)
haigla.patsiendiList.append(Patsient4)

haigla.ArstidList.append(Arstid1)
haigla.ArstidList.append(Arstid2)


print("-----------------------------Patsiendid------------------------------------")
haigla.patsiendideKuuvamine()
print("\n-----------------------------Arstid------------------------------------")
haigla.arstideKuuvamine()
