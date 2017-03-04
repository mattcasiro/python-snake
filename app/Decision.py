def decide(board):
    our_snake = board.our_snake
    
    # bad_squares = getBadSquares()
    valid_moves = { 'left': True,
                    'right': True,
                    'up': True,
                    'down': True }

    directions = ['left','right','up','down']

    for direction in directions:
        if our_snake.moves[direction] in board.get_bad_squares:
            valid_moves[direction] = False

    

    return {
        'move': random.choice(valid_moves),
        'taunt': 'For Noodle!'
    }
