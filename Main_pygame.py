import pygame
import sys
import time
from snake_logic import SnakeGame

CELL_SIZE = 40
GRID_WIDTH, GRID_HEIGHT = 20, 15
FPS = 15

def load_assets():
    assets = {}
    
    names = [
        'apple', 'body_horizontal', 'body_vertical', 'body_topleft', 'body_topright',
        'body_bottomleft', 'body_bottomright', 'head_up', 'head_down', 'head_left',
        'head_right', 'tail_up', 'tail_down', 'tail_left', 'tail_right'
    ]
    
    for name in names:
        path = f"Graphics/{name}.png"
        assets[name] = pygame.image.load(path)
    return assets    

def get_segment_image(game, index, assets):
    dir_name = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    current = game.snake[index]
    
    #cabeça
    if index == 0:
        full_dir = dir_name[game.current_direction]
        return assets[f'head_{full_dir}']
    
    def get_rel_dir(neighbor, curr): #função pra tratar o wrapping
        dx = neighbor[0] - curr[0]
        dy = neighbor[1] - curr[1]
        # Ajuste de wrapping
        if dx > 1: dx = -1
        elif dx < -1: dx = 1
        if dy > 1: dy = -1
        elif dy < -1: dy = 1
        return dx, dy
    
    #cauda
    if index == len(game.snake) - 1:
        prev = game.snake[index - 1] # Segmento anterior
        
        # dx, dy indicam onde o segmento ANTERIOR está em relação à CAUDA
        dx, dy = get_rel_dir(prev, current)
        
        # Se o anterior está para CIMA (dy=-1), a ponta da cauda deve apontar para BAIXO (down)
        # Se o anterior está para BAIXO (dy=1), a ponta da cauda deve apontar para CIMA (up)
        # Se o anterior está para a ESQUERDA (dx=-1), a ponta da cauda aponta para DIREITA (right)
        # Se o anterior está para a DIREITA (dx=1), a ponta da cauda aponta para ESQUERDA (left)
        
        if dy == -1: dir = 'down'   # Anterior em cima -> Ponta para baixo
        elif dy == 1: dir = 'up'    # Anterior embaixo -> Ponta para cima
        elif dx == -1: dir = 'right' # Anterior na esquerda -> Ponta para direita
        else: dir = 'left'           # Anterior na direita -> Ponta para esquerda
        
        return assets[f'tail_{dir}']

    #corpo
    prev = game.snake[index - 1]
    nxt = game.snake[index + 1]
    
    # Direção do anterior e do próximo em relação ao atual
    d1x, d1y = get_rel_dir(prev, current)
    d2x, d2y = get_rel_dir(nxt, current)

    # 1. Corpo Reto
    if d1x == d2x: return assets['body_vertical']
    if d1y == d2y: return assets['body_horizontal']

    # 2. Curvas (Mapeamento exato baseado nos seus assets)
    # Se um vizinho está à esquerda (-1,0) e outro acima (0,-1) -> Curva Top-Left
    if (d1x == -1 and d2y == -1) or (d2x == -1 and d1y == -1):
        return assets['body_topleft']
    
    # Se um vizinho está à direita (1,0) e outro acima (0,-1) -> Curva Top-Right
    if (d1x == 1 and d2y == -1) or (d2x == 1 and d1y == -1):
        return assets['body_topright']
    
    # Se um vizinho está à esquerda (-1,0) e outro abaixo (0,1) -> Curva Bottom-Left
    if (d1x == -1 and d2y == 1) or (d2x == -1 and d1y == 1):
        return assets['body_bottomleft']
    
    # Se um vizinho está à direita (1,0) e outro abaixo (0,1) -> Curva Bottom-Right
    if (d1x == 1 and d2y == 1) or (d2x == 1 and d1y == 1):
        return assets['body_bottomright']

    return assets['body_horizontal'] # Fallback
def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    clock = pygame.time.Clock()
    assets = load_assets()
    game = SnakeGame(GRID_WIDTH, GRID_HEIGHT)
    
    while True:
        new_dir = game.current_direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: new_dir = 'w'
                if event.key == pygame.K_DOWN: new_dir = 's'
                if event.key == pygame.K_LEFT: new_dir = 'a'
                if event.key == pygame.K_RIGHT: new_dir = 'd'
        
        game.move(new_dir) 
        if not game.is_alive:
            print("Morreu"); time.sleep(2); break       
            
        screen.fill((40, 40, 40))
        
        for f in game.fruits:
           screen.blit(pygame.transform.scale(assets['apple'], (CELL_SIZE, CELL_SIZE)), (f[0]*CELL_SIZE, f[1]*CELL_SIZE))
           
        for i in range(len(game.snake)):
            img = get_segment_image(game, i, assets)
            pos = game.snake[i]
            screen.blit(pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE)), (pos[0]*CELL_SIZE, pos[1]*CELL_SIZE))  
            pygame.display.flip()
            clock.tick(FPS)
            
if __name__ == "__main__":
    main()               