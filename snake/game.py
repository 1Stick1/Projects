import numpy as np
import random
import os
import time
import keyboard
import sys

class Field():
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.field = np.full((self.height, self.width), fill_value=' ')
        
    def show_field(self):
        os.system('clear')
        for i in range(self.width):
            print('_', end='  ')
        print('\n')

        for row in self.field:
            for char in row:
                print(char, end='  ')
            print('|\n')

        for i in range(self.width):
            print('_', end='  ')
        print('\n')

    def spawn_apples(self):
        y = random.randrange(0, self.height)
        x = random.randrange(0, self.width)
        if not np.any(self.field == '#') and not field.field[y, x] == '@':
            self.field[y, x] = '#'
            
class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__body = np.zeros((2,2), dtype='int32')
        self.score = 0
        
    def move(self, direction, field):
        new_x, new_y = self.x, self.y
        if direction == 'up':
            new_y = (self.y-1) % field.height
        elif direction == 'down':
            new_y = (self.y+1) % field.height
        elif direction == 'left':
            new_x = (self.x-1) % field.width
        elif direction == 'right':
            new_x = (self.x+1) % field.width
        
    #check if snake go to yourself
        if np.any(np.all(self.__body == [new_y, new_x], axis=1)):
            print(f'Score: {self.score}')
            print("GAME OVER")
            sys.exit()

    #check appple
        apple = field.field[new_y, new_x] == '#'
        
    #add new head
        self.__body = np.insert(self.__body, 0, [self.y, self.x], axis=0)
        self.x, self.y = new_x, new_y
        field.field[self.y][self.x] = '@'
    
        if apple:
            self.score += 1
        else:
            tail = self.__body[-1]
            field.field[tail[0], tail[1]] = ' '
            self.__body = self.__body[:-1]

field = Field(10, 10)
fps = 6
snake = Snake(4, 4)

direction = ''
while True:
    time.sleep(1 / fps)
    field.show_field()
    field.spawn_apples()
    if keyboard.is_pressed('w') and direction != 'down':
        direction = 'up'
    elif keyboard.is_pressed('s') and direction != 'up':
        direction = 'down'
    elif keyboard.is_pressed('a') and direction != 'right':
        direction = 'left'
    elif keyboard.is_pressed('d') and direction != 'left':
        direction = 'right'
    if direction:
        snake.move(direction, field)
    print(f'Score: {snake.score}')