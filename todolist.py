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


uloziste=[]
k="y"

while k=="y" or k=="Y":
    vypis_ukolu(uloziste)
    task=input("Vlož nový úkol:  ")
    u=Ukol(task)
    uloziste.append(u)
    k=input("Chceš přidat další úkol? [Y/N]")
    vymaz_obrazovku()

vypis_ukolu(uloziste)



