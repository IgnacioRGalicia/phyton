import math
import random

class Player:
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
                if val not in game.available_move():
                    raise ValueError
                valid_square = True # if these are successful, then yay
            except ValueError:
                print('Invalid square. Try again.')

        return val