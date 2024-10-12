"""Python code for creating a ecosystem with object oriented code"""
import random

__author__ = "Nikola_Oljaca"


class ecosystem:
    def __init__(self, rounds):
        self.rounds = rounds


class habitat:
    def __init__(self, größe, w_faktor, r_faktor):

        self.größe = größe
        self.w_faktor = w_faktor
        self.r_faktor = r_faktor

    def reproduktion(self):
        self.r_faktor += 0.10
        if self.r_faktor > 1.1:
            self.r_faktor = 0
        else:
            return self.r_faktor


class pflanzenart1(ecosystem, habitat):

    def art(self):
        return self.art

    def __init__(self, größe, rounds, art):
        self.art = art
        self.größe = größe
        self.rounds = rounds

    def grow(self):
        if self.größe == None:
            pass
        else:
            if self.größe < 10000:
                self.größe += 30
            else:
                pass

    def age(self):
        if self.rounds == None:
            pass
        else:
            self.rounds += 1
            return self.rounds

    def die(self, min_größe=10):
        if self.rounds == None:
            pass
        else:
            if self.rounds > 30 or min_größe > self.größe:
                self.art = None
                self.größe = None
                self.rounds = None
            else:
                pass

    def __repr__(self):
        return f"({self.rounds}, {self.art}, {self.größe})"

    def randomdeath(self):
        if random.choice([0, 1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2:
            self.art = None
            self.größe = None
            self.rounds = None
        else:
            pass

    def gefressenwerden(self):
        if self.größe == None:
            pass
        else:
            x = random.choice([0, 5, 10])
            self.größe = self.größe - x
        return self.größe

    def größe(self):
        if self.größe == None:
            self.größe = 0
            return self.größe
        else:
            größe = self.größe
            return größe


class pflanzenart2(ecosystem, habitat):

    def __init__(self, größe, rounds, art):
        self.art = art
        self.größe = größe
        self.rounds = rounds

    def art(self):
        return self.art

    def grow(self):
        if self.größe == None:
            pass
        else:
            if self.größe < 10000:
                self.größe += 30
            else:
                pass

    def age(self):
        if self.rounds == None:
            pass
        else:
            self.rounds += 1
            return self.rounds

    def die(self, dieage=20, min_größe=10):
        if self.rounds == None:
            pass
        else:
            if self.rounds > 30 or min_größe > self.größe:
                self.art = None
                self.größe = None
                self.rounds = None
            else:
                pass

    def __repr__(self):
        return f"({self.rounds}, {self.art}, {self.größe},)"

    def randomdeath(self):
        if random.choice([0, 1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2:
            self.art = None
            self.größe = None
            self.rounds = None
        else:
            pass

    def gefressenwerden(self, x):
        if self.größe == None:
            pass
        else:
            self.größe = self.größe - x
        return self.größe


class pflanzenart3(ecosystem, habitat):

    def __init__(self, größe, rounds, art):
        self.art = art
        self.größe = größe
        self.rounds = rounds

    def art(self):
        return self.art

    def grow(self):
        if self.größe == None:
            pass
        else:
            if self.größe < 10000:
                self.größe += 30
            else:
                pass

    def age(self):
        if self.rounds == None:
            pass
        else:
            self.rounds += 1
            return self.rounds

    def die(self, dieage=100, min_größe=10):
        if self.rounds == None:
            pass
        else:
            if self.rounds > 30 or min_größe > self.größe:
                self.art = None
                self.größe = None
                self.rounds = None
            else:
                pass

    def __repr__(self):
        return f"({self.rounds}, {self.art}, {self.größe},)"

    def randomdeath(self):
        if random.choice([0, 1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2:
            self.art = None
            self.größe = None
            self.rounds = None
        else:
            pass

    def gefressenwerden(self, x):
        if self.größe == None:
            pass
        else:
            self.größe = self.größe - x
        return self.größe


class pflanzen():

    def __init__(self, size):
        self.pflanzeen = []
        self.size = size
        self.index = 0

    def add_pflanzen(self, pflanze):
        self.pflanzeen.append(pflanze)

    def __add__(self, other):
        if not isinstance(other, pflanzenart1):
            if not isinstance(other, pflanzenart2):
                if not isinstance(other, pflanzenart3):
                    raise TypeError("Nur Pflanzen in pflanze erlaubt")
        new_pflanzen = pflanzen(self.size)
        for pflanze in self.pflanzeen:
            new_pflanzen.add_pflanzen(pflanze)
        new_pflanzen.add_pflanzen(other)
        return new_pflanzen

    def __rad__(self, other):
        return self + other

    def __iter__(self):
        return iter(self.pflanzeen)

    def __next__(self):
        if self.index > len(self.pflanzeen):
            raise StopIteration
        new_pflanze = next(self)
        self.index += 1
        return new_pflanze


class Pflanzenfresser():

    def __init__(self, art, rounds, r_rate, nahrung):
        self.art = art
        self.rounds = rounds
        self.r_rate = r_rate
        self.nahrung = nahrung

    def age(self):
        if self.rounds == None:
            pass
        else:
            self.rounds += 1
        return self.rounds

    def die(self):
        if self.rounds == None:
            pass
        else:
            if self.rounds > 50 or self.nahrung < 0:
                self.art = None
                self.rounds = None
                self.r_rate = None
                self.nahrung = None

    def reproduktion(self):
        if self.r_rate == None:
            pass
        else:
            self.r_rate += 0.5
            if self.r_rate >= 1.5:
                self.r_rate = 0
            else:
                return self.r_rate

    def art(self):
        return self.art

    def nahrung(self):
        self.nahrung -= 10
        return self.nahrung

    def frisst(self):
        self.nahrung += 10

    def __repr__(self):
        return f"({self.rounds}, {self.art}, {self.nahrung},)"


class pflanzenfresserliste():
    def __init__(self, size):
        self.pflanzenfressser = []
        self.size = size
        self.index = 0

    def add_pflanzenfresser(self, pflanzenfresser):
        self.pflanzenfressser.append(pflanzenfresser)

    def remove_pflanzenfresser(self):
        if pflanzenfresser == 0:
            pass
        else:
            self.pflanzenfressser.pop()

    def __rad__(self, other):
        return self + other

    def __iter__(self):
        return iter(self.pflanzenfressser)


class Allesfresser(Pflanzenfresser):

    def __init__(self, art, rounds, r_rate, nahrung):
        self.art = art
        self.rounds = rounds
        self.r_rate = r_rate
        self.nahrung = nahrung

    def age(self):
        if self.rounds == None:
            pass
        else:
            self.rounds += 1
        return self.rounds

    def die(self):
        if self.rounds == None:
            pass
        else:
            if self.rounds > 50 or self.nahrung < 0:
                self.art = None
                self.rounds = None
                self.r_rate = None
                self.nahrung = None

    def reproduktion(self):
        if self.r_rate == None:
            pass
        else:
            self.r_rate += 0.2
            if self.r_rate > 2:
                self.r_rate = 0
            else:
                return self.r_rate

    def frisst(self):
        self.nahrung += 20

    def nahrung(self):
        if self.nahrung == None:
            self.nahrung -= 10

    def art(self):
        return self.art

    def __repr__(self):
        return f"({self.rounds}, {self.art}, {self.nahrung},)"

    def jagd(self):
        x = random.choice([0, 1, 3, 4, 5, 4, 3, 4, 3])
        if x == 1:
            return 1
        else:
            return 0


class allesfresserliste():

    def __init__(self, size):
        self.allesfressser = []
        self.size = size
        self.index = 0

    def add_allesfresser(self, allesfresser):
        self.allesfressser.append(allesfresser)

    def remove_allesfresser(self):
        self.allesfressser.pop()

    def __rad__(self, other):
        return self + other

    def __iter__(self):
        return iter(self.allesfressser)


class Fleischfresser(Allesfresser):

    def __init__(self, art, rounds, r_rate, nahrung):
        self.art = art
        self.rounds = rounds
        self.r_rate = r_rate
        self.nahrung = nahrung

    def age(self):
        if self.rounds == None:
            pass
        else:
            self.rounds += 1
        return self.rounds

    def die(self):
        if self.rounds == None:
            pass
        else:
            if self.rounds > 50 or self.nahrung < 0:
                self.art = None
                self.rounds = None
                self.r_rate = None
                self.nahrung = None

    def reproduktion(self):
        if self.r_rate == None:
            pass
        else:
            self.r_rate += 0.2
            if self.r_rate > 1.4:
                self.r_rate = 0
            else:
                return self.r_rate

    def frisst(self):
        self.nahrung += 20

    def nahrung(self):
        if self.nahrung == None:
            pass
        else:
            self.nahrung -= 10

    def art(self):
        return self.art

    def __repr__(self):
        return f"({self.rounds}, {self.art}, {self.nahrung},)"

    def jagd(self):
        x = random.choice([0, 1])
        if x == 1:
            return 1
        else:
            return 0


class fleischfresserliste():

    def __init__(self, size):
        self.fleischfressser = []
        self.size = size
        self.index = 0

    def add_fleischfresser(self, fleischfresser):
        self.fleischfressser.append(fleischfresser)

    def remove_fleischfresser(self):
        self.fleischfressser.pop()

    def __rad__(self, other):
        return self + other

    def __iter__(self):
        return iter(self.fleischfressser)


pflanze_1 = pflanzenart1(200, 0, "Tulpe")
pflanze_2 = pflanzenart2(400, 0, "Baum")
pflanze_3 = pflanzenart3(400, 0, "Busch")
tier_1 = Pflanzenfresser("Koalabär", 0, 0, 100)
tier_2 = Allesfresser("Schwein", 0, 0, 100)
tier_3 = Fleischfresser("Löwe", 0, 0, 100)
x = int(input("Bitte geben Sie die Anzhal der Runden an"))
tulpen_zahl = int(input("Bitte geben Sie di Anzahl an Tulpen an"))
busch_zahl = int(input("Bitte geben Sie di Anzahl an Buschen an"))
baum_zahl = int(input("Bitte geben Sie die Anzahl an Bäumen an"))
koa_zahl = int(input("Bitte geben Sie die Anzahl an Koalas an"))
schwein_zahl = int(input("Bitte geben Sie die Anzahl an Schweinen an"))
löw_zahl = int(input("Bitte geben Sie die Anzahl an Löwen an"))
h_größe = int(input("Bitte geben Sie die Habitatgröße an"))
pflanzeen = pflanzen(500000)
for i in range(tulpen_zahl):
    pflanzeen.add_pflanzen(pflanze_1)
for i in range(busch_zahl):
    pflanzeen.add_pflanzen(pflanze_2)
for i in range(baum_zahl):
    pflanzeen.add_pflanzen(pflanze_3)
pflanzenfresser = pflanzenfresserliste(40000)
for i in range(koa_zahl):
    pflanzenfresser.add_pflanzenfresser(tier_1)
allesfressser = allesfresserliste(400000)
for i in range(schwein_zahl):
    allesfressser.add_allesfresser(tier_2)
fleischfresser = fleischfresserliste(4000)
for i in range(löw_zahl):
    fleischfresser.add_fleischfresser(tier_3)
Habitat = habitat(h_größe, 2, 0)
biomasse = 0

for i in range(x):
    biomasse = 0
    print("round", i)
    for j in pflanzeen:
        biomasse += pflanzenart1.größe(j)
        print(biomasse)
        if Habitat.größe > biomasse:
            if not isinstance(j, pflanzenart1):
                pass
                if not isinstance(j, pflanzenart2):
                    pass
                    if not isinstance(j, pflanzenart3):
                        pass

                    else:
                        pflanzenart3.grow(j)
                        pflanzenart3.age(j)
                        pflanzenart3.die(j)
                        pflanzenart3.randomdeath(j)
                        Habitat.reproduktion()
                        if Habitat.r_faktor > 1:
                            pflanzeen.add_pflanzen(pflanzenart3(400, 0, "Busch"))
                        else:
                            pass
                else:
                    pflanzenart2.grow(j)
                    pflanzenart2.die(j)
                    pflanzenart2.age(j)
                    pflanzenart2.randomdeath(j)
                    Habitat.reproduktion()
                    if Habitat.r_faktor > 1:
                        pflanzeen.add_pflanzen(pflanzenart2(400, 0, "Baum"))
                    else:
                        pass
            else:
                pflanzenart1.grow(j)
                pflanzenart1.age(j)
                pflanzenart1.die(j)
                pflanzenart1.randomdeath(j)
                Habitat.reproduktion()
                print(Habitat.r_faktor)
                if Habitat.r_faktor > 1:
                    pflanzeen.add_pflanzen(pflanzenart1(200, 0, "Tulpe"))
                else:
                    pass
        else:
            pflanzenart1.age(j)
            pflanzenart1.die(j)
    for p in pflanzenfresser:
        Pflanzenfresser.age(p)
        Pflanzenfresser.die(p)
        Pflanzenfresser.reproduktion(p)
        if Pflanzenfresser.reproduktion == 1:
            pflanzenfresser.add_pflanzenfresser(tier_1)
        else:
            pass
        if Pflanzenfresser.art(p) != None:
            Pflanzenfresser.frisst(p)
            for j in pflanzeen:
                pflanzenart1.gefressenwerden(j)
    for a in allesfressser:
        Allesfresser.age(a)
        Allesfresser.die(a)
        if Allesfresser.reproduktion(a) == 1:
            allesfressser.add_allesfresser(tier_2)
        Allesfresser.nahrung(a)
        if Allesfresser.reproduktion == 1:
            allesfressser.add_allesfresser(tier_2)
        else:
            pass
        if Allesfresser.art(a) != None:
            x = random.choice([0, 5, 10])
            if x != 0:
                Allesfresser.frisst(a)
                for j in pflanzeen:
                    pflanzenart2.gefressenwerden(j, x)
            else:
                if Allesfresser.jagd(a) == 1:
                    Allesfresser.frisst(a)
                    if allesfressser == 0:
                        pass
                    else:
                        if pflanzenfresser == 0:
                            pass
                        elif pflanzenfresser == 0:
                            pass
                        else:
                            pflanzenfresser.remove_pflanzenfresser()
        for f in fleischfresser:
            Fleischfresser.age(f)
            Fleischfresser.die(f)
            Fleischfresser.reproduktion(f)
            Fleischfresser.nahrung(f)
        if Fleischfresser.reproduktion == 1:
            fleischfresser.add_fleischfresser(tier_3)
        else:
            pass
        if Fleischfresser.art(f) != None:
            if Fleischfresser.jagd(f) == 1:
                Fleischfresser.frisst(f)
                if allesfressser == 0:
                    pass
                else:
                    allesfressser.remove_allesfresser()

m = 0
n = 0
s = 0
l = 0
for j in pflanzeen:
    if pflanzenart1.art(j) == None:
        pass
    elif pflanzenart2.art(j) == None:
        pass
    elif pflanzenart3.art(j) == None:
        pass
    else:
        m += 1
print(f"Im Habitat leben", {m}, "Pflanzen mit einer Biomasse von", {biomasse})
for i in pflanzenfresser:
    if Pflanzenfresser.art(i) == None:
        pass
    else:
        n += 1
print(f"Im Habitat leben", {n}, "glückliche Koalbären")
for i in allesfressser:
    if Allesfresser.art(i) == None:
        pass
    else:
        s += 1
print(f"Im Habitat leben", {s}, "glückliche Schwein")
for i in fleischfresser:
    if Fleischfresser.art(i) == None:
        pass
    else:
        l += 1
print(f"Im Habitat leben", {l}, "glückliche Löwen")
