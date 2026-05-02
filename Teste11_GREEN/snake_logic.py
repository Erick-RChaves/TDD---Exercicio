import random

class SnakeGame:
    def __init__(self, width, height):
            self.width = width
            self.height = height
            self.snake = [(0,0)]
            self.fruits = []
            self.is_alive = True
            self.spawn_fruits()
            
    def move(self, direction):
        x, y = self.snake[0]
        dirs = {'w': (0,-1), 's':(0,1), 'a': (-1,0), 'd': (1,0)}
        dx, dy = dirs[direction]
        new_head = ((x + dx) % self.width, (y+dy) % self.height)
        self.snake.insert(0,new_head)
        self.snake.pop()
        
    def spawn_fruits(self):
        max = (len(self.snake) // 10) + 1
        while len (self.fruits) < max:
            f = (random.randint(0, self.width-1), random.randint(0, self.height-1))
            if f not in self.snake and f not in self.fruits:
                self.fruits.append(f)
            
      