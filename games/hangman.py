import random
#from wordsfile import words # I dont know why it didnt word 
words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","accept","acceptable","accessible","accidental","account","accurate","achiever","acid","acidic","acoustic","acoustics","acrid","act","action","activity","actor","actually"]
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # keep track of whats already been guessed

    lives = 8
    # getting user input
    while len(word_letters) > 0 and lives > 0:
            # letters used
            # ' '.join(['a', 'b', 'cd']) --> 'a b cd' when run
        print("tienes", lives, "vidas restantes y has usado estas letras: ", " ".join(used_letters))
            # what of the current word has already been guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a lettter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print ("That letter is not in the word.")
        elif user_letter in used_letters:
            print(" U have already guessed that one, choose another")
        else:
            print( " Thats not a valid caracter")
    # U exit the while loop when lives == 0 OR len(word_lettes) == 0
    if lives == 0:
        print("You died. The word was: ", word)
    else:
        print("Youve got it, it was ", word)

hangman()