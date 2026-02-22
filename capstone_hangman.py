import random
import string

# create a list of words


def create_word_list(filename):
    open_file = open(filename, 'r')
    line = open_file.readline()
    word_list = []
    while line != "":
        word_list.append(line.strip('\n'))
        line = open_file.readline()
    open_file.close()
    return word_list


def create_variables():
    available_guesses = []
    for char in string.ascii_lowercase:
        available_guesses.append(char)
    unavailable_guesses = []
    incorrect_guess_count = 0
    return available_guesses, unavailable_guesses, incorrect_guess_count
# choose a word from the list and create the variable that gradually reveals the word
# working


def select_word_and_generate_guess_tracker(word_list):
    word = random.choice(word_list)
    revealed_word = []
    for i in range(len(word)):
        revealed_word.append("_")
    return word, revealed_word

# working


def display_revealed_word(revealed_word, guess_word):
    print("The word is:")
    display = ""
    for item in revealed_word:
        display += item + " "
    print((display))


# working


def display_previous_guesses(unavailable_guesses):
    print("Your have already guessed:")
    display = ''
    for item in sorted(unavailable_guesses):
        display += item + ' '
    if display == '':
        print('No guesses yet.')
        return
    print(display)
    return

# input from user
# working


def input_guess():
    return input("Please guess a letter: ").lower()


def check_valid_guess(current_guess, available_guesses):
    if current_guess not in available_guesses or len(current_guess) > 1:
        print("Invalid guess, please try again")
        return False
    return True

# checks

# function handles a valid guess, and


def handle_valid_guess(current_guess, available_guesses, unavailable_guesses, guess_word, revealed_word):
    unavailable_guesses.append(current_guess)
    available_guesses.remove(current_guess)
    if current_guess not in guess_word:
        global incorrect_guess_count
        incorrect_guess_count += 1

    else:
        for i in range(len(guess_word)):
            if guess_word[i] == current_guess:
                revealed_word[i] = current_guess

# creates a dictionary to store all the images of the hanged man, corresponding to number of lives
# I know the man looks a little strange, but its good enough for now.


def create_hanged_man():
    hanged_man_images = {0: "",
                         1: ("|", "|", "|", "|"),
                         2: ("___", "|", "|", "|", "|"),
                         3: ("___", "| O", "|", "|", "|"),
                         4: ("___", "| O", "| ^", "|", "|"),
                         5: ("___", "| O", "| ^", "| |", "|"),
                         6: ("___", "| O", "| ^", "| |", "| ^")}
    return hanged_man_images
# main function to play the game


def print_hanged_man(hanged_man_images, incorrect_guess_count):
    print()
    for item in hanged_man_images[incorrect_guess_count]:
        print(item)


def check_win(revealed_word, guess_word):
    word = ''
    for item in revealed_word:
        word += item
    if word == guess_word:
        return True
    return False


def display_win_message(guess_word, incorrect_guess_count):
    print("Congratulations, you win.")
    print(
        f"You got the word {guess_word} with {incorrect_guess_count} mistakes")


def display_failure_message():
    global guess_word
    print("You ran out of lives")
    print("The man has been hanged")
    print(f"The word you were looking for was {guess_word}")
    print("Better luck next time")

# main program


# first create all variables used in the program
word_list = create_word_list('words_alpha.txt')
available_guesses, unavailable_guesses, incorrect_guess_count = create_variables()
guess_word, revealed_word = select_word_and_generate_guess_tracker(word_list)
hanged_man_images = create_hanged_man()
# print a pretty title
print("----------WELCOME TO HANGMAN----------")
# initialise the gameplay loop
while check_win(revealed_word, guess_word) == False:

    display_revealed_word(revealed_word, guess_word)
    display_previous_guesses(unavailable_guesses)
    current_guess = input_guess()
    # restarts the gameplay loop if an invalid guess is made
    if check_valid_guess(current_guess, available_guesses) == False:
        continue

    handle_valid_guess(current_guess, available_guesses, unavailable_guesses,
                       guess_word, revealed_word)
    print_hanged_man(hanged_man_images, incorrect_guess_count)
    print('')
    if incorrect_guess_count == 6:
        break
if check_win(revealed_word, guess_word) == True:
    display_win_message(guess_word, incorrect_guess_count)
else:
    display_failure_message()
