import random, datetime
import Taunt
def first_five(board):
    try:
        five_file = open('movefile.txt', 'w')
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
            #five_file.write('right\ndown\nleft')
            five_file.write('right\n')
            five_file.write('down\n')
            five_file.write('left\n')
            return 'up'
        elif valid_moves['up'] and valid_moves['left']:
            #five_file.write('left\ndown\nright')
            five_file.write('left\n')
            five_file.write('down\n')
            five_file.write('right\n')
            return 'up'
        elif valid_moves['down'] and valid_moves['right']:
            #five_file.write('right\nup\nleft')
            five_file.write('right\n')
            five_file.write('up\n')
            five_file.write('left\n')
            return 'down'
        else:
            #five_file.write('left\nup\nright')
            five_file.write('left\n')
            five_file.write('up\n')
            five_file.write('right\n')
            return 'down'
    except IOError as e:
        print(e)
    finally:
        five_file.close()

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
    #for direction in directions:
    #    if (valid_moves[direction] and 
    #    ([our_snake.moves[direction][0] - 1, our_snake.moves[direction][1]] in board.get_bad_squares())):
        #and [our_snake.moves[direction][0] + 1, our_snake.moves[direction][1]]
        #and [our_snake.moves[direction][0], our_snake.moves[direction][1] - 1]
        #and [our_snake.moves[direction][0], our_snake.moves[direction][1] + 1]
        #    valid_moves[direction] = False;
    

    # preferred moves (like targeting food)
    preferred_moves = { 'left': False,
                    'right': False,
                    'up': False,
                    'down': False }
    if our_snake.health < 30:
        # target food
        if our_snake.head[0] < nearest_food[0]:
            preferred_moves['right'] = True;
        elif our_snake.head[0] > nearest_food[0]:
            preferred_moves['left'] = True;

        if our_snake.head[1] < nearest_food[1]:
            preferred_moves['down'] = True;
        if our_snake.head[1] > nearest_food[1]:
            preferred_moves['up'] = True;
    else:
        pass
    
    print preferred_moves
    print valid_moves

    print(board.game_turn)

    #pick a move
    choice = 'left'
    for move in valid_moves:
        if preferred_moves[move]:
            choice = move
    if not valid_moves[choice]:
        for move in valid_moves:
            if valid_moves[move]:
                choice = move

    print choice

    t1 = datetime.datetime.now()
    if board.game_turn == 0:
        choice = first_five(board)
        print("first five returned {}" .format(choice))
    elif board.game_turn < 4:
        try:
            five_file = open('movefile.txt', 'r')
            move_list = []
            for move in five_file:
                print("adding " + move)
                move_list.append(move)
            print("first five contained: {}" .format(move_list))
            choice = move_list[board.game_turn - 1]
            choice = choice[:-1]
            print("first five chose: {}" .format(choice))
        except IOError as e:
            print(e)
        finally:
            five_file.close()

    t2 = datetime.datetime.now()
    td = t2 - t1
    print(td.total_seconds())
    print(choice)
    
    taunt = Taunt.Taunt()
    return {
        'move': choice,
        'taunt': taunt.grab_taunt()
    }
