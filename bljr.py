# Definisikan class Animal
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

# Definisikan class Cat sebagai turunan dari class Animal
class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

    def suara(self):
        return "meow!"

# Buat instance dari kelas Cat bernama "myCat"
myCat = Cat(name="Neko", age=3, species="Persian")

# Contoh penggunaan method dan akses ke atribut
print(myCat.deskripsi())  # Output: "Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun"
print(myCat.suara())      # Output: "meow!"
