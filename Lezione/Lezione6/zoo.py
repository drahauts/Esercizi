class Zoo:
    def __init__(self, fences:int, zoo_keepers: str) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

"""
2. Animal: questa classe rappresenta un animale nello zoo.
Ogni animale ha questi attributi: name, species, age, height,
width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
"""

class Animal:
    def __init__(self, name: str, species: str, age: float, height: float, width: float, preferred_habitat: str, health: int):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)

    def __str__(self) -> str:
        return f"Animal(nome - {self.name}, specie - {self.species}, età - {self.age}, altezza - {self.height}, larghezza - {self.width}, habbitat preferito - {self.preferred_habitat}, stato della salute - {self.health})"


"""
3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali.
I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
"""

class Fence:
    def __init__(self, area: float, tempreature: float, habitat: str) -> None:
        self.area = area
        self.tempreature = tempreature
        self.habitat = habitat


"""
ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo.
I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali,
pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.
"""


class ZooKeeper:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(animal: Animal, fence: Fence):
        pass

"""
1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale):
consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo.
L'animale deve essere collocato in un recinto adeguato in base alle esigenze
del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del
recinto è ancora sufficiente per ospitare questo animale.
"""