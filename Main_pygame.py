import pygame
import sys
from snake_logic import SnakeGame

assets  = {
    'head_up' : pygame.image.load('Graphics/head_up.png'),
    'head_down' : pygame.image.load('Graphics/head_down.png'),
    'head_right' : pygame.image.load('Graphics/head_right.png'),
    'head_left' : pygame.image.load('Graphics/head_left.png'),
    'body_bottomleft' : pygame.image.load('Graphics/body_bottomleft.png'),
    'body_bottomright' : pygame.image.load('Graphics/body_bottomright.png'),
    'body_horizontal' : pygame.image.load('Graphics/body_horizontal.png'),
    'body_topleft' : pygame.image.load('Graphics/body_topleft.png'),
    'body_topright' : pygame.image.load('Graphics/body_topright.png'),
    'body_vertical' : pygame.image.load('Graphics/body_vertical.png'),
    'tail_down' : pygame.image.load('Graphics/tail_down.png'),
    'tail_left' : pygame.image.load('Graphics/tail_left.png'),
    'tail_right' : pygame.image.load('Graphics/tail_right.png'),
    'tail_up' : pygame.image.load('Graphics/tail_up.png'),
    'apple' : pygame.image.load('Graphics/apple.png')
}

def get_segment_image(game, index, assets):
    current = game.snake[index]
    
    #cabeça
    if index == 0:
        return assets[f'head_{game.current_direction}']
    
    #cauda
    if index == len(game.snake) - 1:
        previous = game.snake[index -1]
        dx, dy = previous[0] - current[0], previous[1] - current[1]
        
        if dx > 1: dx= -1
        elif dx < -1: dx = 1
        if dy > 1: dy = -1
        elif dy < -1: dy = 1
        dir = 'up' if dy == -1 else 'down' if dy == 1 else 'left' if dx == -1 else 'right'
        return assets[f'tail_{dir}']
    
    #corpo
    previous, next = game.snake[index-1], game.snake[index + 1]
    p_dx, p_dy = previous[0] - current[0], previous[1] - current[1]
    n_dx, n_dy = next[0] - current[0], next[1] - current[1]
    
    if abs(p_dx) > 1: p_dx = -1 if p_dx > 0 else 1
    if abs(n_dx) > 1: n_dx = -1 if n_dx > 0 else 1
    if abs(p_dy) > 1: p_dy = -1 if p_dy > 0 else 1
    if abs(n_dy) > 1: n_dy = -1 if n_dy > 0 else 1
    
    if p_dx == n_dx: return assets['body_vertical']
    if p_dy == n_dy: return assets['body_horizontal']
    
    return assets['body_horizontal']
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        screen.fill((0, 0, 0))
        screen.blit(assets['head_up'], (100, 100))
        pygame.display.update()
        clock.tick(60)