import pytest
from snake_logic import SnakeGame


def test_game_inicialization():
    game = SnakeGame(width = 10, height = 15)
    assert game.width == 10
    assert game.height == 15
    assert len(game.snake) == 1
    assert game.is_alive == True
    
@pytest.mark.parametrize("cmd, expected", [
    ('d', (1,5)), ('a',(-1,5)),
    ('w', (0,4)), ('s', (0,6))
])    
def test_directions(cmd, expected):
    game = SnakeGame(10,10)
    game.snake = [(0, 5)]
    game.move(cmd)
    assert game.snake[0] == expected   