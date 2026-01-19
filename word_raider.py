import random
game_title = "word_raider"
#set up a list of words to choose 
word_bank=[]
#open the file bank
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())
#pick a random word from the list
word_to_guess = random.choice(word_bank)
#print(word_to_guess)
#set up the game variables
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0
#display the current state of the game
print("Welcome to", game_title)
print("The word has", len(word_to_guess), "letters")
print("You have", max_turns - turns_taken, "turns left")
#build the game loop
while turns_taken < max_turns:
    The_guess = input("Guess a word: ").lower() 
#check if the guess length is equal to the length og the game
    if len(The_guess) < len(word_to_guess) or not The_guess.isalpha():
        print("Please enter a five letter word.")
        continue
#check if each letter in the guess against the word's letter
    index = 0
    for c in The_guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
                print("_", end=" ")
        else:
         if c not in incorrect_guesses:
             incorrect_guesses.append(c)
        print(".", end=" ")
        index += 1

    print("\n")
    print("Misplaced letters: ", misplaced_guesses)
    print("incorrect letters: ", incorrect_guesses)
    #increment turn
    turns_taken += 1
    #check if the player has won
    if The_guess == word_to_guess:
        print("Congratulations🏆🏆, you win!!")
        break
    #check if the play has lost
    if turns_taken == max_turns:
        print(f"You lose😫 the word was: {word_to_guess}")
        
    #display the number of turns left and ask for another guess
    print("You have", max_turns - turns_taken,"turns left.")
    
