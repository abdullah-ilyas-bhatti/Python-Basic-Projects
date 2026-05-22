import random 
stages = [
    """
       +---+

       |   |
       O   |
      /|\\  |
      / \\  |

           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      /    |


           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |


           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|   |


           |
           |
     =========
    """,
    """
       +---+


       |   |
       O   |


       |   |
           |


           |
     =========
    """,
    """
       +---+

       |   |
       O   |


           |
           |
           |
     =========
    """,
    """
       +---+


       |   |
           |


           |
           |
           |
     =========
    """
]


print("Welcome to the Hangman Game")
print("Guss a word and fill the blanks | Note: You Have only 6 Chances ")
words=[

    "banana", "giraffe", "jacket", "monster", "pumpkin", "rocket", "spider", "zebra",
    "astronaut", "blizzard", "cyclone", "dolphin", "flavored", "galaxy", "mystery", "whisper",
    "awry", "crypt", "frizz", "glow", "haiku", "ivory", "jazz", "jinx", "myth", "oxide", "sphinx",
    "acknowledge", "bookkeeper", "duplex", "equinox", "gossip", "hyphen", "jaywalk", "megahertz", "pneumonia", "psychology", "quartz", "subway", "xylophone",
    "ballyhoo", "bumfuzzled", "brouhaha", "cattywampus", "dingus", "gobbledygook"
]
lives=6
hangman_word=random.choice(words)

length=len(hangman_word)

placeholder=""
for dash in range(length):
    placeholder+="_ "
print(placeholder)
list=[]
game_over= False
while not game_over:
    
    guess_word=input("Guess a Word: ")
    display=""
    for letter in hangman_word:
        if letter == guess_word:
            display+=letter
            list.append(guess_word)
        elif letter in list:
            display+=letter
        else:
            display+=" _ "
    if " _ " not in display:
        game_over=True
        print("Wow! You won")
    if guess_word not in hangman_word:
        lives -= 1
        print(f"You Have Remaining Chances {lives}/6")
    if lives == 0:
        game_over=True
        print("You Lose all Chances , Game Over ")
    print(display)
    print(stages[lives])

 
