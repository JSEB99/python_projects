# Hangman Game brr
import random
import Hangman_words
import Hangman_art

print(Hangman_art.logo)
chosen_word = random.choice(Hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already wrote {guess}, try again")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not a correct letter")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(Hangman_art.stages[lives])
