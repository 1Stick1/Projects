import random
import time

class Hero():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = {'Heal': 2,}

    def attack(self, other):
        critical = random.randint(self.damage - 4, self.damage + 4)
        time.sleep(2)
        print(f'{self.name} attacks {other.name}')

        if critical < self.damage:
            print(f'Attack!! {self.name} slipped. -{critical}')
        else:
            print(f'Attack!! {self.name} make critical damage. -{critical}')
        other.take_damage(critical)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            print(f'{self.name} dead.')
            self.health = 0

    def heal(self):
        if(self.inventory['Heal'] > 0):
            self.health += 20
            self.inventory['Heal'] -= 1
            print(f'{self.name} is using heal. +20hp')
        else:
            print(f'{self.name} haven\'t heal anymore')
    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f'{self.name} health: {self.health}'

class Mage(Hero):
    def __init__(self, name): 
        super().__init__(name, health = 70, damage = 20)
        self.mana = 100
        self.inventory['Mana'] = 3
        
    def attack(self, other):
        base_critical = random.randint(self.damage - 4, self.damage + 4)
        critical = base_critical
        time.sleep(2)
    
        print(f'{self.name} attacks {other.name}')

        if self.mana >= 40:
            self.mana -= 40
            critical += 30
            print(f'{self.name} attacks with magical damage {other.name}')
        else:
            print(f'{self.name} attacks with common damage. Not enough mana')

        if base_critical < self.damage:
            print(f'Attack!! {self.name} slipped. -{critical}')
        elif base_critical > self.damage:
            print(f'Attack!! {self.name} make critical damage. -{critical}')
        else:
            print(f"Attack!! -{critical}")      
        other.take_damage(critical)
        
    
    def __str__(self):
        return f'{super().__str__()}, Mana: {self.mana}'
    
class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, health = 110, damage = 25)
        self.name = name
    def take_damage(self, amount):
        if random.random() < 0.3:
            amount -= 10
            print(f'{self.name} blocks 10 damage!')
        amount = max(0, amount)
        super().take_damage(amount)

class Rogue(Hero):
    def __init__(self, name):
        super().__init__(name, health = 90, damage = 35)
        self.name = name
    def take_damage(self, amount):
        if random.random() < 0.25:
            amount = 0
            print(f"{self.name} dodged the attack")
        super().take_damage(amount)

class Player():
    def __init__(self, player):
        self.player = player
    def turn(self, enemy):
        action = input('Enter action:\n1. Attack\n2. Heal\n3. Skip\n')
        print('\n')
        
        if action == '1':
            self.player.attack(enemy)
        elif action == '2':
            self.player.heal()
        elif action == '3':
            pass
        print('\n\n')
        print(enemy)
        print(self.player)
class Enemy():
    def __init__(self, enemy):
        self.enemy = enemy
    def turn(self, player):
        action = random.randrange(1,3)
        print('\n')
        if action == 1:
            self.enemy.attack(player)
        elif action == 2:
            self.enemy.heal()
        print('\n\n')
        print(player)
        print(self.enemy)
    
def fight(player, enemy):
    print(f"\n\n\n\tFight is starting! {player.name} vs {enemy.name}\n")
    print(player)
    print(enemy)
    print('\n')
    while player.is_alive() and enemy.is_alive():
        if player.is_alive():
            player1.turn(enemy)
            time.sleep(4)

        print('\n')

        if enemy.is_alive():
            enemy1.turn(player)
            time.sleep(4)
    if player.health == 0:
        print(f'{enemy.name} win!!')
    else:
        print(f'{player.name} win!!')

mage = Mage('Mage')
warrior = Warrior('Warrior')
player1 = Player(warrior)
enemy1 = Enemy(mage)
fight(warrior, mage)
print(mage)
