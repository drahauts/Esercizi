class Charachter:

    def __init__(self, level: int) -> None:
        self.level = level
        self.health = self.base_hp * level
        self.attack_power = self.base_attack_power * level

    def attack(self):
        print(f"{self.base_name}: attacks with {self.attack_power} power")

    def __str__(self) -> str:
        return f"{self.base_name} (level - {self.level}, health - {self.health})"
    

class Ork(Charachter):
    base_hp = 100
    base_attack_power = 10
    base_name = "Ork"

class Elf(Charachter):
    base_hp = 50
    base_attack_power = 15
    base_name = "Elf"

    def attack(self):
        print("This method in the class-father")

elf_1 = Elf(level= 1)
print(elf_1)
elf_1.attack()
print("=======================")
ork_1 = Ork(level= 1)
print(ork_1)
ork_1.attack()