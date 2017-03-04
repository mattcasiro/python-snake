def decide(board):
    snake = board.our_snake
    
    # bad_squares = getBadSquares()
    valid_moves = [ 'left' : true,
                    'right' : true,
                    'up' : true,
                    'down' : true]


    for spot, move in bad_squares:
        if spot in snake.moves:
            valid_moves[move] = false;

    

    return {
        'move': random.choice(valid_moves),
        'taunt': 'For Noodle!'
    }
