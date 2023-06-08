import random

def hangman():

    word_list = ['happy', 'cat', 'python', 'java', 'javascript', 'hacker', 'painter', 'computer', 'developer', 'software', 'umbrella', 'music', 'juggling', 'skating', 'spelunking', 'outside', 'spring', 'coding', 'fun']
    list_length = len(word_list) - 1
    random_number = random.randint(0, list_length)
    word = word_list[random_number]
    
    wrong_guesses = 0
    stages = ['',
             ' ________       ',
             '|        |      ',
             '|        0      ',
             '|       /|\     ',
             '|       / \     ',
             '|               '
              ]
    
    remaining_letters = list(word)
    board = ['__'] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong_guesses < len(stages) - 1:
        print('\n')
        message = 'Guess a letter: '
        guess = input(message)
        
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1

        print((' '.join(board)))
        slice_end = wrong_guesses + 1
        print('\n'.join(stages[0: slice_end]))

        if '__' not in board:
            print('\n')
            print('You win!')
            print(' '.join(board))
            win = True
            break
        
    if not win:
        print('\n'.join(stages[0: slice_end]))
        print('\n')
        print('You lose! It was {}.'.format(word))

hangman()
