# Turn-Based Battle System

## Project Overview

This project is a Python turn-based battle game where the player chooses a character class and battles against an Evil Wizard.

The player can choose actions during each turn, such as attacking, healing, using special abilities, or viewing stats. After each player turn, the Evil Wizard regenerates health and attacks back. The game continues until either the player defeats the wizard or the wizard defeats the player.

## Features

* Choose from multiple character classes:

  * Warrior
  * Mage
  * Archer
  * Paladin

* Turn-based battle system

* Randomized attack damage

* Healing system

* Character stats display

* Special abilities for certain classes

* Evil Wizard regeneration after each player turn

* Victory and defeat messages

## Character Classes

### Character

The `Character` class is the base class. It contains shared attributes and methods that all characters use, such as:

* `name`
* `health`
* `attack_power`
* `max_health`
* `attack()`
* `heal()`
* `display_stats()`

### Warrior

The Warrior has high health and strong attack power.

### Mage

The Mage has lower health but higher attack power.

### Archer

The Archer has special abilities:

* `quick_shot()` — temporarily doubles attack power for one attack.
* `evade()` — allows the Archer to evade the wizard’s next attack.

### Paladin

The Paladin has high health and defensive abilities:

* `holy_strike()` — increases attack power for one attack.
* `divine_shield()` — blocks the wizard’s next attack.

### Evil Wizard

The Evil Wizard is the enemy. It can:

* Attack the player.
* Regenerate health after each player turn.

## How the Game Works

1. The player chooses a character class.
2. The player enters their character name.
3. The battle begins against the Evil Wizard.
4. Each turn, the player chooses one action:

   * Attack
   * Use Special Ability
   * Heal
   * View Stats
5. If the wizard is still alive after the player’s turn, the wizard regenerates health.
6. The wizard then attacks the player unless the player is evading or blocking.
7. The game ends when either the player or the wizard reaches 0 health.

## How to Run the Project

Make sure Python is installed on your computer.

Then run the file in the terminal:

```bash
python main.py
```

Depending on your system, you may need to use:

```bash
python3 main.py
```

## Example Gameplay

```text
Choose your character class:
1. Warrior
2. Mage
3. Archer
4. Paladin

Enter the number of your class choice: 3
Enter your character's name: Darwin

--- Your Turn ---
1. Attack
2. Use Special Ability
3. Heal
4. View Stats
Choose an action:
```

The player continues choosing actions until the battle ends.

## Technologies Used

* Python
* Object-Oriented Programming
* Classes and inheritance
* Random number generation
* User input
* Conditional logic
* Loops

## What I Learned

While building this project, I practiced:

* Creating and using classes
* Using inheritance to share code between character types
* Writing methods for attacks, healing, and special abilities
* Using a while loop to keep the battle running
* Handling user input
* Creating win and loss conditions
* Using random damage to make gameplay less predictable

## Future Improvements

Possible future improvements include:

* Adding special abilities for Warrior and Mage
* Adding more enemies
* Adding difficulty levels
* Adding inventory or items
* Improving the battle menu
* Adding replay functionality
* Preventing character health from going below zero

## Author

Darwin Rubio
