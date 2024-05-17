class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = ["Sword", "Shield", "Heal Pot"]
        self.level = 1

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

class Enemy:
    def __init__(self, name, health, attackPower):
        self.name = name
        self.health = health
        self.attackPower = attackPower

    def attack(self, player):
        player.takeDamage(self.attackPower)

class Info:
    def __init__(self):
        return 0
    
   


def main():
    print("-------------------------------------------\n|          Welcome to the RPG!            |\n-------------------------------------------")
    
player_name = input("Enter your character's name: ")
player = Player(player_name)

def charInfo():
        print("")
        print("Your name is: " + str(player.name))
        print("Health: " + str(player.health))
        print("Inventory: "+ str(player.inventory))
        print("Level: " + str(player.level))
        print("")




if 1 == 1:
    main()
