class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("Ciao, sono {} {}.".format(self.nome, self.cognome))

class Studente(Persona):
    def saluta(self):
        print("Buongiorno, sono lo studente {} {}.".format(self.nome, self.cognome))

class Professore(Persona):
    def saluta(self):
        print("Salve a tutti.")
    def saluta_informale(self):
        super().saluta()

Blaz = Studente('Blaz', 'Petejan')
Blaz.saluta()

Nastja = Persona('Nastja', 'Ferluga')
Nastja.saluta()

Matteo = Professore('Matteo', 'Gallet')
Matteo.saluta()
Matteo.saluta_informale()

print(issubclass(Studente, Persona))
print(issubclass(Professore, Persona))
print(issubclass(Persona, Studente))