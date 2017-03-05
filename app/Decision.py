import random
def decide(board):
    our_snake = board.our_snake
    nearest_food = board.nearest_foods[our_snake.id]

    directions = ['left','right','up','down']



    # DONT HIT A WALL OR A SNAKE
    valid_moves = { 'left': True,
                    'right': True,
                    'up': True,
                    'down': True }
    for direction in directions:
        # NOTE: call get_bad_squares() once if response time issue
        if our_snake.moves[direction] in board.get_bad_squares():
            valid_moves[direction] = False


    #check surrounding squares of each 'valid_move'
    for direction in directions:
        if valid_moves[direction] && [our_snake.moves[direction][0] - 1, our_snake.moves[direction][1]]:
            valid_moves[direction] = False;
        if valid_moves[direction] && [our_snake.moves[direction][0] + 1, our_snake.moves[direction][1]]:
            valid_moves[direction] = False;
        if valid_moves[direction] && [our_snake.moves[direction][0], our_snake.moves[direction][1] - 1]:
            valid_moves[direction] = False;
        if valid_moves[direction] && [our_snake.moves[direction][0], our_snake.moves[direction][1] + 1]:
            valid_moves[direction] = False;
    

    # preferred moves (like targeting food)
    preferred_moves = { 'left': False,
                    'right': False,
                    'up': False,
                    'down': False }
    # target food
    if our_snake.head[0] < nearest_food[0]:
        preferred_moves['right'] = True;
    elif our_snake.head[0] > nearest_food[0]:
        preferred_moves['left'] = True;

    if our_snake.head[1] < nearest_food[1]:
        preferred_moves['down'] = True;
    if our_snake.head[1] > nearest_food[1]:
        preferred_moves['up'] = True;
    print preferred_moves
    print valid_moves


    #pick a move
    for move in valid_moves:
        if preferred_moves[move]:
            choice = move
    if not valid_moves[choice]:
        for move in valid_moves:
            if valid_moves[move]:
                choice = move

    print choice

    return {
        'move': choice,
        'taunt': our_snake.id
    }
