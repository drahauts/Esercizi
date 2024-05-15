class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat, health: None) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age) * 3)

class Fence:    # Recinto
    def __init__(self, area, temperetature, habitat) -> None:
        self.area = area
        self.temperetature = temperetature
        self.habitat = habitat
        self.animals = []
        self.totale_conto = area


class ZooKeeper:
    def __init__(self, name, surname, id) -> None:
        self.name = name
        self.surname = surname
        self.id = id
        

    def add_animal(self, animal: Animal, fence: Fence):
        animal_area = animal.width * animal.height
        if animal.preferred_habitat == fence.habitat and fence.area > animal_area :
            fence.animals.append(animal)
            print(f"L'animale {animal.name} e stato aggiunto al nuovo recinto {fence.habitat}")
        else:
            print(f"L'animale {animal.name} non puo essere aggiunto al recinto {fence.habitat}")
        
    def remove_animal(self, animal: Animal, fence: Fence):
        # area_animal = animal.width * animal.height
        # fence_area= fence.width * fence.height
        # new_fence_area = area_animal + fence_area
        if animal in fence.animals:
            fence.animals.remove(animal)
            # fence.area = new_fence_area
            print(f"Animale {animal.name} è stato corretamente tolto dal recinto {fence.habitat}")
        else:
            print(f"Animale {animal.name} non è presente nel recinto {fence.habitat}")
        

    

    def feed(self, animal: Animal):
        if self.fence.area >= animal.area:
            animal.health += 1
            animal.width *= 1.02
            animal.height *= 1.02
            self.fence.area -= animal.area
            print(f"Animale {animal.name} e stato nutrito con sucesso")
        else:
            print(f"Animale {animal.name} non può essere nutrito ")

    def clean_fence(self, fence: Fence):
        index_trash: float = 0.0
        
        if fence and isinstance(fence, Fence):
            if fence.area > 0:
                index_trash =  (fence.totale_conto - fence.area)/ fence.area 
            elif fence.area == 0:
                index_trash = fence.totale_conto
            
            return index_trash
    

    def describe_zoo(self):
        print("Guardini dello Zoo: ")
        for guardini in self.zoo_keepers:
            print(f"Nome - {guardini.name}\nCognome - {guardini.surname}\nId: {guardini.id}")
        
        print("I recinti dello Zoo: ")
        for recinti in self.fences:
            print(f"Recinti:\nArea - {recinti.area}\nTemperatura - {recinti.temprerature}\nHabitat - {self.habitat}")
        
        print("Animali dello Zoo: ")
        for animale in self.animals:
            print(f"Nome {animale.name}, specie - {animale.species}")

class Zoo:
    def __init__(self, fences = None, zoo_keepers = None) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers


guardiano = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
lion = Animal("Leo", "Lion", 5, 1.5, 2, "Savannah", None)
fence1 = Fence(100, 25, "Savannah")

guardiano.add_animal(lion, fence1)
guardiano.remove_animal(lion, fence1)
#guardiano.feed(lion)
print(guardiano.clean_fence(fence1))