import random
from PyDictionary import PyDictionary

dictionary = PyDictionary()

# Set up the dictionary of letters and their point values
letter_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
                 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
                 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

# Set up the bag of tiles
tile_bag = ['A']*9 + ['B']*2 + ['C']*2 + ['D']*4 + ['E']*12 + ['F']*2 + ['G']*3 + \
           ['H']*2 + ['I']*9 + ['J']*1 + ['K']*1 + ['L']*4 + ['M']*2 + ['N']*6 + \
           ['O']*8 + ['P']*2 + ['Q']*1 + ['R']*6 + ['S']*4 + ['T']*6 + ['U']*4 + \
           ['V']*2 + ['W']*2 + ['X']*1 + ['Y']*2 + ['Z']*1
random.shuffle(tile_bag)

# Set up the players and their tiles
players = {'Player 1': [], 'Player 2': []}
for i in range(7):
    for player in players:
        players[player].append(tile_bag.pop())

# Define a function to calculate the score for a word
def calculate_score(word):
    score = 0
    for letter in word:
        score += letter_values[letter]
    return score

# Main game loop
current_player = 'Player 1'
while True:
    print(current_player + "'s turn.")
    print("Your tiles are:", " ".join(players[current_player]))
    word = input("Enter your word (or 'pass' to skip): ").upper()
    if word == 'PASS':
        # Give the player a new tile and switch to the other player
        players[current_player].append(tile_bag.pop())
        current_player = 'Player 2' if current_player == 'Player 1' else 'Player 1'
    elif not all(letter in players[current_player] for letter in word):
        print("You don't have all those letters!")
    else:
        # Calculate the score and update the player's tiles
        score = calculate_score(word)
        print("Score for", word + ":", score)
        for letter in word:
            players[current_player].remove(letter)
            if not tile_bag:
                break
            players[current_player].append(tile_bag.pop())
        if not tile_bag:
            break