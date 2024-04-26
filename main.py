from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")


class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука")


class Fighter:
    def __init__(self, weapon=None):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"Боец выбрал: {self.weapon.__class__.__name__}")

    def fight(self):
        self.weapon.attack()


class Monster:
    def affected(self):
        print("Монстр побежден!")


fighter = Fighter()
monster1 = Monster()
monster2 = Monster()

fighter.change_weapon(Sword())
fighter.fight()
monster1.affected()
fighter.change_weapon(Bow())
fighter.fight()
monster2.affected()
