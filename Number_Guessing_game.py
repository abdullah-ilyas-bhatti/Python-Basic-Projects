import random
numbers=list(range(1,101))
thinking_number=random.choice(numbers)

game_over=False
def play_game():
    global game_over
    print("welcome to the Number Guessing game")
    print("I am Tinking of a number between 1 and 100 ")
    choice=input("choose  a dificulity Type 'easy' or 'hard': ")
    if choice == "easy":
        attempts=10
        print(f"You have {attempts} attempts remaining to guess the Number ")
        while not game_over:
            guessing_number=int(input("Make a guess: "))
            if guessing_number == thinking_number:
                print("Wow You guess a Exact word which i Think") 
                game_over=True
            elif guessing_number > thinking_number:
                attempts -=1
                print("Too High")
                print("Guess again")
                print(f"You have {attempts} attempts remaining to guess the Number ")
            elif guessing_number < thinking_number:
                attempts -=1
                print("Too Low")
                print("Guess again")
                print(f"You have {attempts} attempts remaining to guess the Number ")
            if attempts == 0:
                print("You Lose  Game Over ")
                game_over=True
    else:
        attemptss=7
        print(f"You have {attemptss} attempts remaining to guess the Number ")
        while not game_over:
            guessing_number=int(input("Make a guess: "))
            if guessing_number == thinking_number:
                print("Wow You guess a Exact word which i Think  You Win") 
                game_over=True
            elif guessing_number > thinking_number:
                attemptss -=1
                print("Too High")
                print("Guess again")
                print(f"You have {attemptss} attempts remaining to guess the Number ")
            elif guessing_number < thinking_number:
                attemptss -=1
                print("Too Low")
                print("Guess again")
                print(f"You have {attemptss} attempts remaining to guess the Number ")
            if attemptss == 0:
                print("You Lose  Game Over ")
                game_over=True
        
play_game()
