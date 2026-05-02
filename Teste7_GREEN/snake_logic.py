class SnakeGame:
    def __init__(self, width, height):
            self.width = width
            self.height = height
            self.snake = [(0,0)]
            self.is_alive = True
            
    def move(self, direction):
        x, y = self.snake[0]
        dirs = {'w': (0,-1), 's':(0,1), 'a': (-1,0), 'd': (1,0)}
        dx, dy = dirs[direction]
        new_head = (x + dx, y+dy)
        self.snake.insert(0,new_head)
        self.snake.pop()
      