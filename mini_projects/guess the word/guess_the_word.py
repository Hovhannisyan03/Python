import random
from collections import Counter

some_words = '''Yerevan NewYork Tokyo London Paris Berlin Sydney Cairo Rome Madrid Moscow Lisbon Mumbai Dubai Melbourne Barcelona SaoPaulo Toronto CapeTown LosAngeles MexicoC BuenosAires Seoul Bangkok Jakarta Riyadh'''

# create a list using split
some_words = some_words.split(' ')

# randomly choose a secret word from our "some_words"
word = random.choice(some_words)

# start game
print('Guess the word! HINT: word is a name of a city')
print('Press 0 if you want to exit')

for _ in word:
    print('_', end=' ')
print()

play = True
guessed_letters = ''
chance_to_play = len(word) + 3
corrct = 0
flag = 0

try:
    while chance_to_play != 0 and flag == 0:
        print()
        chance_to_play -= 1
        try:
            your_guess = str(input("Enter a letter: ")) 
            if(your_guess == '0'):
                print("Bye!")
                break
        except:
            print("Enter only letter!")
            continue
        if not your_guess.isalpha():
            print("Enter only letter!")
            continue
        elif len(your_guess) > 1:
            print("Enter only one letter")
            continue
        elif your_guess in guessed_letters:
            print("You have already guessed that letter")

        # If letter is guessed correctly
        if your_guess.lower() in word or your_guess.upper() in word:
            lower_count = word.count(your_guess.lower())
            for _ in range(lower_count):
                guessed_letters += your_guess.lower()
            
            upper_count = word.count(your_guess.upper())
            for _ in range(upper_count):
                guessed_letters += your_guess.upper()
            
        for char in word:
            if char in guessed_letters and Counter(guessed_letters) != Counter(word):
                print(char, end = ' ')
            elif Counter(guessed_letters) == Counter(word):
                print(f"You won, the word is: {word}")
                flag = 1
                break
            else:
                print('_', end = ' ')

    # If user has used all of his chances
    if chance_to_play <= 0 and (Counter(guessed_letters) != Counter(word)):
        print()
        print("You lost, try again")
        print(f"The word was {word}")    
except KeyboardInterrupt:
    print()
    print('Bye! Try again.')
    exit()
