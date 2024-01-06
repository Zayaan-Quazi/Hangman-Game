import random
from collections import Counter

Animals = "ZEEBRA TIGER LION GIRAFFE WOLF"
Words = Animals.split()
chosen_word = random.choice(Words)
Guessed_Letters = ""
print(chosen_word)

no_of_chances = len(chosen_word) + 2 

for letter in chosen_word:
    print("_", end=" ")

word_guessed = False

while no_of_chances != 0 and not word_guessed:
    
    print()  
    guess = input(f"Enter a letter. You have {no_of_chances} chances to guess the correct word: ").upper()
    print()

    if len(guess) == 1 and guess.isalpha():
        
        if guess in Guessed_Letters:
            print("You have already guessed that letter")
            no_of_chances = no_of_chances - 1
            print(f"You have {no_of_chances} chances")

        elif guess in chosen_word:
            no_of_chances -= 1
            Guessed_Letters += guess
            print("Great guess!")
        
        else:
            no_of_chances -= 1
            print("Incorrect guess.")

        # Display the word with guessed letters
        for letter in chosen_word:
            if letter in Guessed_Letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        # Check if all letters are guessed correctly
        if Counter(Guessed_Letters) == Counter(chosen_word):
            print(f"\nCongratulations! You guessed the word: {chosen_word}")
            word_guessed = True

    else:
        no_of_chances -= 1
        print("Please enter a valid single letter.")
        

# If chances run out
if no_of_chances == 0 and not word_guessed:
    print(f"\nSorry, you're out of chances. The word was: {chosen_word}")

