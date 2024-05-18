from character import Player

def welcome():
    print("----------------------------------------------")
    print("|            Welcome to the RPG!             |")
    print("----------------------------------------------")

def charInfo(player):
    print("\n              Your Character:")
    print("----------------------------------------------")
    print(f"Name:      {player.name}")
    print(f"Health:    {player.health}")
    print(f"Race:      {player.race}")
    print(f"Class:     {player.Class}")
    print(f"Inventory: {player.inventory}")
    print(f"Level:     {player.level}")
    print(f"Coins:     {player.coins}")
    print(f"Defense:   {player.defense}")
    print(f"Damage:    {player.damage}")
    print("----------------------------------------------\n")

def main():
    welcome()

    name = input("Enter your character's Name: ").title()
    Class = input("Enter your character's Class: ").capitalize()

    # Mage Class adjustment 
    if Class == "Mage":
        inventory = ["Staff"]
    else:
        inventory = ["Sword", "Shield"]

    # Player Character
    mainChar = Player(name = name, health = 100, race = "Human", Class = Class, inventory = inventory, level = 1, coins = 100, damage = 1, defense = 1)

    # Item Stats
    for item in mainChar.inventory:
        if item == "Sword":
            mainChar.damage += 1
        elif item == "Shield":
            mainChar.defense += 1
        elif item == "Staff":
            mainChar.damage += 2

    # Class Stat Buffs
    if Class == "Warrior":
        mainChar.defense += mainChar.level
    elif Class == "Mage":
        mainChar.damage += mainChar.level
    elif Class == "Paragon":
        mainChar.damage += 0.5 * mainChar.level
        mainChar.defense += 0.5 * mainChar.level

    charInfo(mainChar)

if 1 == 1:
    main()
