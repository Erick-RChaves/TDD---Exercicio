class SnakeGame:
    def __init__(self, width, height):
            self.width = width
            self.height = height
            self.snake = [(0,0)]
            self.is_alive = True