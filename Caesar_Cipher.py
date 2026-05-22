alphabets=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print("Welcome to the Caesar Cipher")


def ceasar(message ,number ,ed ):
    cipher_text=""
    if ed == "decode":
        number *= -1
    for letter in message:
        if letter not in alphabets:
            cipher_text+=letter
        else:
            shifted_text = alphabets.index(letter) + number
            shifted_text %= len(alphabets)
            cipher_text += alphabets[shifted_text]
    print(f"Here is your {ed} Message: {cipher_text}")

condition=True
while condition:
    choose=input("Type 'Encode' to Encrypt or 'Decode' to Decrypt: \n").lower()
    msg=input("Type Your Message: \n").lower()
    num=int(input("Type your Shift Number: \n"))
    ceasar(msg, num, choose)
    restart=input("type 'yes' if you want go again otherwise type 'no': \n").lower()
    if restart == "no":
        condition=False
        print("Good_Bye")
    
    
    
    
    
    
    
    
    
    
    
