import random
import time
import os

quantity_fights = 0
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
            message = f'Attack!! {self.name} slipped. -{critical}'
            print(message)
        else:
            message = f'Attack!! {self.name} make critical damage. -{critical}'
            print(message)
        write_to_file(message)
        other.take_damage(critical)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            message = f'{self.name} dead.'
            write_to_file(message)
            print(message)
            self.health = 0

    def heal(self):
        if(self.inventory['Heal'] > 0):
            self.health += 20
            self.inventory['Heal'] -= 1
            message = f'{self.name} is using heal. +20hp'
            print(message)
        else:
            message = f'{self.name} haven\'t heal anymore'
            print(message)
        write_to_file(message)
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
            print(f"{self.name} dodged the attack!")
        super().take_damage(amount)
temp = 0
def enemy_turn(enemy, player):
    action = random.randrange(1,4)
    global temp
    print('\n')
    if action == 1 or action == 2:
        enemy.attack(player)
    elif action == 3 and temp <= 3:
        temp += 1
        enemy.heal()
    print('\n\n')
    print(player)
    print(enemy)

def player_turn(player, enemy):
        action = input('Enter action:\n1. Attack\n2. Heal\n3. Skip\n')
        print('\n')
        if action == '1':
            player.attack(enemy)
        elif action == '2':
            player.heal()
        elif action == '3':
            pass
        print('\n\n')
        print(enemy)
        print(player)
   
def fight(player, enemy):
    os.makedirs('fights-log', exist_ok=True)
    os.chdir('./fights-log')
    global quantity_fights 
    quantity_fights += 1
    
    os.system('cls||clear')
    print(f"\n\n\n\tFight is starting! \n\n\t{player.name}(You) vs {enemy.name}\n")
    print(player)
    print(enemy)
    print('\n')
    round_number = 0
    while player.is_alive() and enemy.is_alive():
        round_number += 1
        print("Round", round_number)
        if player.is_alive():
            player_turn(player, enemy)
            time.sleep(4)

        print('\n')

        if enemy.is_alive():
            enemy_turn(enemy, player)
            time.sleep(4)
    if player.health == 0:
        print(f'{enemy.name} win!!')
    else:
        print(f'{player.name} win!!')

def print_heros():
    print("1. Mage (70hp, 20 attack, 100 mana, 50 attack with mana)")
    print("2. Warrior (110hp, 25 attack, has 30% chance to block 10 points of damage)")
    print("3. Rogue (90hp, 35 attack, has chance 25% to dodge the attack)")

def menu(nickname):
    print("Pick your hero: ")
    print_heros()
    a = input()
    if a == '1':
        player = Mage(nickname)
    elif a == '2':
        player = Warrior(nickname)
    elif a == '3':
        player = Rogue(nickname)

    print("Now choose your enemy: ")
    print_heros()
    a = input()
    
    if a == '1':
        enemy = Mage('Mage(enemy)')
    if a == '2':
        enemy = Warrior('Warrios(enemy)')
    if a == '3':
        enemy = Rogue('Rogue(enemy)')
    
    fight(player, enemy)
    
def write_to_file(message):
    with open(f'fight-{quantity_fights}', 'a') as fight_log:
        fight_log.write(message + '\n')

print("Game 1v1")
nickname = input("Enter your nickname: ")

while True:
    menu(nickname)