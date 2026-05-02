import random

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = [(5, 5), (4, 5), (3, 5)] 
        self.fruits = []
        self.is_alive = True
        self.current_direction = 'd'
        self.spawn_fruits()
            
    def move(self, direction):
        if not self.is_alive: return
        
        
        opposites = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}
        if direction in ['w', 's', 'a', 'd'] and direction != opposites.get(self.current_direction):
            self.current_direction = direction

        x, y = self.snake[0]
        dx, dy = {'w': (0,-1), 's':(0,1), 'a': (-1,0), 'd': (1,0)}[self.current_direction]
        
        
        new_head = ((x + dx) % self.width, (y + dy) % self.height)
        
        if new_head in self.snake:
            self.is_alive = False
            return
        
        self.snake.insert(0, new_head)
        
        if new_head in self.fruits:
            self.fruits.remove(new_head)
            self.spawn_fruits()
        else:
            self.snake.pop()
        
    def spawn_fruits(self):
        max_fruits = (len(self.snake) // 10) + 1
        while len(self.fruits) < max_fruits:
            f = (random.randint(0, self.width-1), random.randint(0, self.height-1))
            if f not in self.snake and f not in self.fruits:
                self.fruits.append(f)
            
      