import random
import string


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}



        
class Player:
    def __init__(slef, points):
        points = ""

p1 = Player(0)
p2 = Player(0)


def score_counter(word, player):
        player.points = 0
        word = word.lower()
        for l in word:
            player.points += score[l]
        print("You scored " + str(player.points) + " points")

def get_winner():
    x = p1.points
    y = p2.points
    if x == y:
        print("It's a tie!")
    elif x > y:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

def play_game():
        print("Here are your letters")
        board = ''.join([random.choice(string.ascii_lowercase) for l in range(16)])
        print(board)
        print("Player 1 make a word.")
        p1_word = input(": ")
        score_counter(p1_word, p1)
        print("Player 2 make a word.")
        p2_word = input(": ")
        score_counter(p2_word, p2)
        get_winner()
        play_again()

def play_again():
    print("Would you like to play again? y or n: ")
    user_input = input(": ")
    if str(user_input) == "y":
        play_game()
    elif str(user_input) == "n":
        quit
    else:
        print(user_input + " is not a valid response.")
        play_again()
        

print("Let's play Boggle!")
play_game()

