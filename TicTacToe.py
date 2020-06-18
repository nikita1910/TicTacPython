import random


class TicTacToeGame:
    def __init__(self):
        self.msg = "\033[1;34mWelcome to Tic Tac Toe!\033[1;m"
        self.default_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']


objGame = TicTacToeGame()


def display_board(board):
    """
     :param board: board values to print
    :return: print board
    """
    print(f'{board[1]}|{board[2]}|{board[3]}')
    print('------')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('------')
    print(f'{board[7]}|{board[8]}|{board[9]}')


def player_input(board):
    """
    :param board: default board values
    :return: nothing
    """
    check_flag = False
    flag = False
    position_list = []
    player1 = ''
    while not flag:
        player1 = input("Player1, please pick a maker 'X' or 'O':\t")
        if player1.upper() == 'X' or player1.upper() == 'O':
            flag = True
        else:
            print('Please enter valid marker.')
    if player1.upper() == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f'Player1: {player1.upper()}\t Player2: {player2.upper()}')
    first_turn = choose_first()
    if first_turn == 1:
        print('Player1 will go first.')
    else:
        print('Player2 will go first.')
    ready_flag = False
    while not ready_flag:
        strYN = input('Are you ready(Y/N)?\t')
        if strYN.upper() == 'Y':
            ready_flag = True
            while not check_flag:
                try:
                    position = int(input(f'Player{first_turn} enter your position(1-9):\t'))
                    while position in position_list:
                        position = int(input(f'Place is already taken. Player{first_turn} enter your new position:\t '))
                    position_list.append(position)
                    if first_turn == 1:
                        maker = player1
                        first_turn = 2
                    else:
                        maker = player2
                        first_turn = 1
                    bool_val = place_maker(board, maker, position)
                    if bool_val:
                        check_flag = True
                    if len(position_list) == 9:
                        break
                except:
                    print('Please enter valid position(1-9)')
            if check_flag:
                if first_turn == 1:
                    first_turn = 2
                else:
                    first_turn = 1
                print('Congratulations!')
                print(f'Player{first_turn} you won. :)')
                replay()
            else:
                print("Ohh! It's a tie.")
                replay()

        elif strYN.upper() == 'N':
            print('Okay! Take your time')
        else:
            print('Please enter valid input.')


def replay():
    """
    :return: play again or not
    """
    test1_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        msg_replay = input('Would you like to play again(Y/N)?\t')
        if msg_replay.upper() == 'Y':
            print('\n' * 100)
            print(objGame.msg)
            display_board(test1_board)
            player_input(test1_board)
            break
        elif msg_replay.upper() == 'N':
            print('Thank you!')
            break
        else:
            print('Please enter valid input(Y/N).')


def win_check(board):
    """
    :param board: board values to check winner
    :return: winner flag
    """
    maker_dict = {'maker1': 'XXX', 'maker2': 'OOO'}

    if (board[1] + board[4] + board[7] == maker_dict['maker1'] or board[1] + board[4] + board[7] == maker_dict[
        'maker2']) \
            or (board[1] + board[2] + board[3] == maker_dict['maker1'] or board[1] + board[2] + board[3] == maker_dict[
        'maker2']) \
            or (board[1] + board[5] + board[9] == maker_dict['maker1'] or board[1] + board[5] + board[9] == maker_dict[
        'maker2']) \
            or (board[3] + board[6] + board[9] == maker_dict['maker1'] or board[3] + board[6] + board[9] == maker_dict[
        'maker2']) \
            or (board[3] + board[5] + board[7] == maker_dict['maker1'] or board[3] + board[5] + board[7] == maker_dict[
        'maker2']) \
            or (board[7] + board[8] + board[9] == maker_dict['maker1'] or board[7] + board[8] + board[9] == maker_dict[
        'maker2']) \
            or (board[2] + board[5] + board[8] == maker_dict['maker1'] or board[2] + board[5] + board[8] == maker_dict[
        'maker2']) \
            or (board[4] + board[5] + board[6] == maker_dict['maker1'] or board[4] + board[5] + board[6] == maker_dict[
        'maker2']):
        win_flag = True
    else:
        win_flag = False

    return win_flag


def choose_first():
    """
    :return: randon number
    """
    return random.randrange(1, 3)


def place_maker(board, maker, position):
    """

    :param board: board numbers
    :param maker: X or O
    :param position: place on the board
    :return: winning flag
    """
    board[position] = maker.upper()
    display_board(board)
    return win_check(board)


if __name__ == '__main__':
    test_board = objGame.default_board  # ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    print(objGame.msg)
    display_board(test_board)
    player_input(test_board)
