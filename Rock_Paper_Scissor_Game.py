import random
options=["rock", "paper", "scissor"]
print("Welcome to the Rock , Paper , Scissor Game")
user_choice=input("Type atleast one rock , paper , scissor:  ").lower()
computer_choice=random.choice(options)
print(f"Computer choose: {computer_choice}")

if computer_choice == user_choice:
    print("Match Tied")
elif computer_choice == "rock" and user_choice== "paper":
    print("Great! You Won ")
elif computer_choice == "rock" and user_choice== "scissor":
    print("Oops! You Lose")
elif computer_choice == "paper" and user_choice== "scissor":
    print("Great! You Won ")
elif computer_choice == "paper" and user_choice== "rock":
    print("Oops! You Lose")
elif computer_choice == "scissor" and user_choice== "rock":
    print("Great! You Won ")
elif computer_choice == "scissor" and user_choice== "paper":
    print("Oops! You Lose")
else:
    print("You write wrong word , something else , check spell and Try again")
