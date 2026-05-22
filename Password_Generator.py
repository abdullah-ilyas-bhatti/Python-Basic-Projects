import random
print("welcome to the Password Generator")
letters=int(input("How many Alphabets you want in Password ? "))
num=int(input("How many Numbers you want in Password ? "))
sign=int(input("How many Symbols you want in Password ? "))
alphabets=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols=[".", ",", "?", "!","-", "_", "(", ")", "+", "-", "*", "/", "=", "<", ">", "%", "@", "#", "$", "&", "^", "~", "|"]
password=[]
for generate in range(0,letters):
    password+=random.choice(alphabets)

for gen in range(0,num):
    password+=random.choice(numbers)

for rate in range(0,sign):
    password+=random.choice(symbols)
print(password)
random.shuffle(password)
print(password)
final_password=""
for char in password:
    final_password+= char
print(f"Best Secure Password for you is: {final_password}")
