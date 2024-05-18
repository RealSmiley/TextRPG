# character.py

class Player:
    def __init__(self, name, health, race, inventory, level, damage, coins, Class, defense):
        self.name = name
        self.health = health
        self.healthMax = health
        self.race = race
        self.inventory = inventory
        self.level = level
        self.damage = damage
        self.coins = coins
        self.Class = Class
        self.defense = defense

    def attack(self, enemy):
        enemy.health -= self.damage
        if enemy.health < 0:
            enemy.health = 0

class Enemy:
    def __init__(self, name, health, level, damage, coins, defense):
        self.name = name
        self.health = health
        self.level = level
        self.damage = damage
        self.coins = coins
        self.defense = defense

    def enemyInfo(self):
        print("\n              Enemy Information:")
        print("----------------------------------------------")
        print(f"Name:      {self.name}")
        print(f"Health:    {self.health}")
        print(f"Level:     {self.level}")
        print(f"Damage:    {self.damage}")
        print(f"Defense:   {self.defense}")
        print("----------------------------------------------\n")
