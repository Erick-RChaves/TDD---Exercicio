import pygame

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