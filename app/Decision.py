import random, datetime
def decide(board):
    our_snake = board.our_snake
    
    # bad_squares = getBadSquares()
    valid_moves = { 'left': True,
                    'right': True,
                    'up': True,
                    'down': True }

    directions = ['left','right','up','down']

    for direction in directions:
        if our_snake.moves[direction] in board.get_bad_squares():
            valid_moves[direction] = False

    for move in valid_moves:
        if valid_moves[move]:
            choice = move
            
    print(board.game_turn)

    t1 = datetime.datetime.now()
    if board.game_turn == 0:
        choice = first_five()
    elif board.game_turn < 4:
        try:
            five_file = open('../resources/movefile.txt', 'r')
            move_list = []
            for move in five_file:
                move_list += move
            choice = move_list[board.game_turn - 1]
        except IOError as e:
            print(e)
        finally:
            five_file.close()

    t2 = datetime.datetime.now()
    td = t2 - t1
    print(td.total_seconds())
    
    return {
        'move': choice,
        'taunt': 'For Noodle!'
    }

def first_five(self):
    try:
        five_file = open('../resources/movefile.txt', 'w')
        our_snake = board.our_snake
        
        valid_moves = { 'left': True,
                        'right': True,
                        'up': True,
                        'down': True }

        directions = ['left','right','up','down']

        for direction in directions:
            if our_snake.moves[direction] in board.get_bad_squares():
                valid_moves[direction] = False

        #Write turtle square moves to move file text
        #Noodle will turtle up and go into a sqaure move pattern for
        #the first few turns. Movement depends on which X and Y directions are clear
        if valid_moves['up'] and valid_moves['right']:
            five_file.write('right\ndown\nleft')
            return 'up'
        elif valid_moves['up'] and valid_moves['left']:
            five_file.write('left\ndown\nright')
            return 'up'
        elif valid_moves['down'] and valid_moves['right']:
            five_file.write('right\nup\nleft')
            return 'down'
        else:
            five_file.write('left\nup\nright')
            return 'down'

    except IOError as e:
        print(e)

    finally:
        five_file.close()
