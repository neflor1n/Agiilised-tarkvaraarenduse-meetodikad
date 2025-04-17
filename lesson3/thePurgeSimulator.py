import random

class Player:
    def __init__(self, hp, energy, food):
        self.hp = hp
        self.energy = energy
        self.food = food

    def status(self):
        print(f"\n[ Staatus ] HP: {self.hp} | Energia: {self.energy} | Toit: {self.food}")

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 3
            print("Sa puhkasid. Energia taastatud (+3).")
        else:
            print("Pole piisavalt toitu puhkamiseks!")

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        print(f"Said kahju: -{dmg} HP.")

    def use_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def add_food(self, amount):
        self.food += amount

    def is_alive(self):
        return self.hp > 0 and self.energy > 0


def random_event():
    roll = random.randint(0, 2)
    if roll == 0:
        return "DANGER"
    elif roll == 1:
        return "FOOD"
    return "NONE"


def process_event(player):
    event = random_event()
    if event == "DANGER":
        print("⚠️  Ohtlik sündmus! Sa sattusid rünnaku alla.")
        player.take_damage(3)
        player.use_energy(1)
    elif event == "FOOD":
        print("🍖 Leidsid toidutagavara! (+1 toidukord)")
        player.add_food(1)
    else:
        print("Kõik on vaikne... midagi ei juhtunud.")


def main():
    player = Player(hp=10, energy=5, food=2)
    day = 1

    print("🎮 Tere tulemast mängu 'Sundöö'!")
    print("Eesmärk: jää ellu nii kaua kui võimalik, tehes strateegilisi otsuseid.")

    while player.is_alive():
        print(f"\n========== Päev {day} ==========")
        player.status()

        print("Valikud:")
        print("1. Puhka (kasutab toitu, taastab energiat)")
        print("2. Riskida sündmusega (võib leida toitu või saada kahju)")
        print("3. Mitte teha midagi (jätad päeva vahele)")

        choice = input("Vali (1-3): ")

        if choice == "1":
            player.rest()
        elif choice == "2":
            process_event(player)
        elif choice == "3":
            print("Sa otsustasid mitte midagi teha...")
            player.use_energy(1)
        else:
            print("❌ Vigane valik.")
            continue

        player.use_energy(1)  # kulub iga päev
        day += 1

    print("\n💀 Mäng läbi. Sa ei jäänud ellu.")
    print(f"Ellujäämispäevad: {day - 1}")


if __name__ == "__main__":
    main()
