import random

def play():
    user = input("Choose one, 'r' for rock, 'p' for paper and 's' for scissors")
    computer = random.choice(['r','p','s'])

    # Esto que viene aquí funciona pero ocupa mucho
    if (user == 'r' and computer == 'r'):
        return 'Rock against Rock. It\'s a tie'
    elif (user == 'r' and computer == 'p'):
        return 'Rock against Paper. You lose jeje'
    elif (user == 'r' and computer == 's'):
        return 'Rock against Scissors. You win!'


    elif (user == 'p' and computer == 'r'):
        return 'Paper against Rock. You win!'   
    elif (user == 'p' and computer == 'p'):
        return 'Paper against Paper .It\'s a tie'   
    elif (user == 'p' and computer == 's'):
        return 'Paper against Scissors. You lose jeje'
    
    
    elif (user == 's' and computer == 'r'):
        return 'Scissors against Rock. You lose jeje'
    elif (user == 's' and computer == 'p'):
        return 'Scissors against Paper. You win!'
    elif (user == 's' and computer == 's'):
        return 'Scissors against Scissors. It\'s a tie'


    if user == computer:
        return ' It is a tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return ' You won!'
    # here you can put, elif is_win(computer, user) but this way it uses one more line of code
    return ' You lost!'

def is_win(player,opponent):
    #return true if the player wins


    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True



    # Esto es muy chapucero pero funciona
    # if (user == 'r' and computer == 'r'):
    #     return 'Rock against Rock. It\'s a tie'
    # elif (user == 'r' and computer == 'p'):
    #     return 'Rock against Paper. You lose jeje'
    # elif (user == 'r' and computer == 's'):
    #     return 'Rock against Scissors. You win!'


    # elif (user == 'p' and computer == 'r'):
    #     return 'Paper against Rock. You win!'   
    # elif (user == 'p' and computer == 'p'):
    #     return 'Paper against Paper .It\'s a tie'   
    # elif (user == 'p' and computer == 's'):
    #     return 'Paper against Scissors. You lose jeje'
    
    
    # elif (user == 's' and computer == 'r'):
    #     return 'Scissors against Rock. You lose jeje'
    # elif (user == 's' and computer == 'p'):
    #     return 'Scissors against Paper. You win!'
    # elif (user == 's' and computer == 's'):
    #     return 'Scissors against Scissors. It\'s a tie'


print(play())