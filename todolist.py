class Ukol:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return self.name

    def komentar_ukolu(self,komentar):
        self.komentar = input("přidej komentář k úkolu")


def vypis_ukolu(depository):
    print("Aktuální úkoly: ")
    for x in depository:
        print(x)


def vymaz_obrazovku():
    print("\n" * 100)

def smaz_ukol(index):
    uloziste.pop(index)

uloziste=[]
k=""


while k!="exit":

    k=input("Pro vkládání úkolů napište libovolný text, pro smazání úkolu napiš smazat, pro vypnutí aplikace napiš exit:  ")
    if k=="smazat":
        i=input("Zadejte číslo úkolu, který si přejete smazat (číslováno od 0): ")
        smaz_ukol(int(i))
        vymaz_obrazovku()
        vypis_ukolu(uloziste)
    elif k!="exit":
        task = input("Vlož nový úkol:  ")
        u = Ukol(task)
        uloziste.append(u)
        vymaz_obrazovku()
        vypis_ukolu(uloziste)


vymaz_obrazovku()
vypis_ukolu(uloziste)
print("Děkujeme, že používáte naši aplikaci.")






