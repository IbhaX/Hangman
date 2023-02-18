import os, sys
from random import choice

cmd = "cls" if sys.platform == "win32" else "clear"
clear = lambda: os.system(cmd)

def hangman(hang):
    level = {0: '''
  +---+
  |   |
  |
  |
  |
  |
=========''', 1: '''
  +---+
  |   |
  |   O
  |
  |
  |
=========''', 2: '''
  +---+
  |   |
  |   O
  |   |
  |
  |
=========''', 3: '''
  +---+
  |   |
  |   O
  |  /|
  |
  |
=========''', 4: '''
  +---+
  |   |
  |   O
  |  /|\\
  |
  |
=========''', 5: '''
  +---+
  |   |
  |   O
  |  /|\\
  |  /
  |
  |
=========''', 6: '''
  +---+
  |   |
  |  O
  |  /|\\
  |  / \\
  |
========='''}
    return level[hang]

def quote():
    quotes = [
       "Look closer. It’s worth it", "You are living your story."
       "No storm can last forever.","Nothing is ours expect time.",
       "Be gentle. First with yourself.",
       "Falling is not always a failure.",
       "Failure is success in progress.",
       "Some things are better unsaid."
       "Before you assume, try asking."
        ]
    return choice(quotes)

def match(word, usr_choice, blank):
    for j in range(len(word)):
        if usr_choice in word[j]:
            blank[j] = usr_choice
    return blank


def get_word(difficulty=1):
    with open("hangman_words.txt") as f:
        data = f.readlines()
    modes = {
                  1: (3, 6), 2: (4, 7), 3: (5, 8),
                  4: (6, 9), 5: (7, 10), 6: (8, 11)
             }
    count = choice(list(range(*modes[difficulty])))
    words = [i.strip() for i in data if len(i) == count]
    word = choice(words)
    return word, ['_' for i in range(len(word))]
    
def display(lives, optional=None):
    clear()
    print("\t\tHangman Game")
    print(optional)
    comment =  f'"{quote()}"'
    print(comment)
    print(hangman(lives))
    
def main():
    print("\t\tHangman Game")
    mode = int(input("Enter difficulty (1 - 6): "))
    word, blank = get_word(mode)
    game_over = False
    lives = 0
    won = False
    comment = None
    
    while not game_over and lives < 6:
        if not comment:
            comment = f"You have to find {len(blank)} letter word!!"
        display(lives, comment)
        blank_str = " ".join(blank)
        print(blank_str)

        usr_choice = input("Enter choice: ")
        if usr_choice in blank:
            comment = "You guessed that already..."
            display(lives, comment)
            
        blank = match(word, usr_choice, blank)
        
        if usr_choice not in word:
            lives += 1
            comment = None
            
        if '_' not in blank:
            game_over = True
            won = True
            
    print(blank_str)
    comment = f'The word is "{word}"'
    display(lives, comment)
    
    print("You won..." if won else "You Lose...")
            
main()
