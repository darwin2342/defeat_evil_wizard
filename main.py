import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(max(1, self.attack_power - 5), self.attack_power + 5)
        opponent.health -= damage
        
        if opponent.health < 0:
            opponent.health = 0

        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 20
        old_health = self.health
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        old_health = self.health
        self.health += 5

        if self.health > self.max_health:
            self.health = self.max_health
        
        actual_regen = self.health - old_health
        print(f"{self.name} regenerates {actual_regen} health! Current health: {self.health}")


# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        self.evading = False

    def quick_shot(self, opponent):
        print(f'{self.name} uses Quick Shot!')

        original_attack_power = self.attack_power
        self.attack_power *= 2
        self.attack(opponent)
        self.attack_power = original_attack_power

    def evade(self):
        self.evading = True
        print(f'{self.name} is evading the next attack!')

    

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.blocking = False
        
    def holy_strike(self, opponent):
        print(f'{self.name} uses Holy Strike!')
        original_attack_power = self.attack_power
        self.attack_power += 10
        self.attack(opponent)
        self.attack_power = original_attack_power

    def divine_shield(self):
        self.blocking = True
        print(f'{self.name} raises a Divine Shield! The next attack will be blocked!')


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                ability_choice = input("Choose a special ability: ")

                if ability_choice == '1':
                    player.quick_shot(wizard)
                elif ability_choice == '2':
                    player.evade()
                else:
                    print("Invalid choice. No special ability used.")
                    continue
            elif isinstance(player, Paladin):
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability_choice = input("Choose a special ability: ")

                if ability_choice == '1':
                    player.holy_strike(wizard)
                elif ability_choice == '2':
                    player.divine_shield()
                else:
                    print("Invalid choice. No special ability used.")
                    continue
            else:
                print(f"{player.name} has no special abilities. Please choose a different action.")
                continue
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")
            continue

        if wizard.health > 0:
            wizard.regenerate()

            if getattr(player, "evading", False):
                print(f"{player.name} evaded the wizard's attack!")
                player.evading = False

            elif getattr(player, "blocking", False):
                print(f"{player.name} blocked the wizard's attack with Divine Shield!")
                player.blocking = False       

            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()