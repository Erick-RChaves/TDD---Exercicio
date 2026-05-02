import pytest
from snake_logic import SnakeGame


def test_game_inicialization():
    game = SnakeGame(width = 10, height = 15)
    assert game.width == 10
    assert game.height == 15
    assert len(game.snake) == 1
    assert game.is_alive == True
    
@pytest.mark.parametrize("cmd, expected", [
    ('d', (1,5)), ('a',(9,5)),
    ('w', (0,4)), ('s', (0,6))
])    
def test_directions(cmd, expected):
    game = SnakeGame(10,10)
    game.snake = [(0, 5)]
    game.move(cmd)
    assert game.snake[0] == expected   
    
def test_tail_follows_head():
    game = SnakeGame(10, 10)
    game.snake = [(1, 0), (0, 0)]
    game.move('d')
    assert game.snake == [(2,0), (1,0)]    
    
def test_wrapping_x():
    game = SnakeGame(10, 10)
    game.snake = [(9,0)]
    game.move('d')
    assert game.snake[0] == (0,0)   
    
def test_wrapping_y():
    game = SnakeGame(10,10)
    game.snake = [(0, 0)] 
    game.move('w')
    assert game.snake[0] == (0, 9)    
    
def test_initial_fruit_exists():
    game = SnakeGame(10, 10)
    assert len(game.fruits) == 1    
    
def test_eat_fruit_and_grow():
    game = SnakeGame(10, 10)
    game.snake = [(5, 5)]
    game.fruits = [(6, 5)]
    game.move('d')
    assert len(game.snake) == 2
    assert (6, 5) not in game.fruits
    
def test_self_collision():
    game = SnakeGame(10, 10)
    game.snake = [(5, 5), (6, 5), (6, 6), (5, 6)]
    game.move('s')
    assert game.is_alive == False
    
def test_multiple_fruits_at_10():
    game = SnakeGame(10,10) 
    game.snake = [(0, 0)] * 10
    game.spawn_fruits()
    assert len(game.fruits) == 2
    
def test_multiple_fruits_at_20():
    game = SnakeGame(20, 20)
    game.snake = [(0, 0)] * 20
    game.spawn_fruits()
    assert len(game.fruits) == 3