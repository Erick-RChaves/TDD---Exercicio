from snake_logic import SnakeGame

def test_game_inicialization():
    game = SnakeGame(width = 10, height = 15)
    assert game.width == 10
    assert game.height == 15
    assert len(game.snake) == 1
    assert game.is_alive == True
    
def test_move_right():
    game = SnakeGame(10,10)
    game.move('d') 
    assert game.snake[0] == (1,0)   