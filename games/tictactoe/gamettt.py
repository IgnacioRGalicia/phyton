# from player import HumanPlayer, RandomComputerPlayer 
# import player

import math
import random
import time

class Player():
    def __init__(self, letter):
    # letter is x or o
        self.letter = letter
    
    #we want all player to get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # se comprueba que el valor es correctamente
            # un integer y será inválido si no lo es. Tambien será
            # invalido si no está disponible el sitio de la tabla
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay
            except ValueError:
                print('Invalid square. Try again.')

        return val
        



class TicTacToe:
    def __init__(self):
        self.board = self.make_board() #we will use a singke list to rep 3x3 board
        self.current_winner = None # keep track if theres a winner 

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3]for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # que numero va en cada sitio
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x'|'x'|'o'] --> [(0, 'x'),(1, 'x'),(2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
        # # todo esto se puede condensar a una linea de codigo
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valed move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere, we have to check all
        # the rows
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all ([spot == letter for spot in row]):
            return True
        # the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True
        # the diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all ([spot == letter for spot in diagonal2]):
                return True

        # if all these fails:
        return False

def play(game, x_player,o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'x' # the starting letter 
    # iterate while the game still has empty square
    while game.empty_squares():
        #getting a move from the appropiate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        #lets define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to squate {square}')
                game.print_board()
                print('') # empty line to add space

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # after we made our move, we need to alternate letters
            letter = 'o' if letter == 'x' else 'x'
        # tiny break to look more human
        time.sleep(0.8)
    if print_game:
        print('its a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)