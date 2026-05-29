logo="""
     _____________________
    |  _________________  |
    | | JO           0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    """
        
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2
    
operators={
"+" : add,
"-" : sub,
"/" : div,
"*" : multiply,
}

def overall_calculation():
    print(logo)
    calculation=True 
    num1=float(input("Enter a First Number: "))
    while calculation:
        print("+ \n- \n/ \n* \n ")
        choose=input("Pick an operator: ")
        num2=float(input("Enter a secound Number: "))
        answer=operators[choose](num1,num2)
        print(f"{num1} {choose} {num2} = {answer} ") 
        choice=input(f"Type 'yes' to continue calculating {answer} , or Type 'no' to exit: ").lower()
        if choice == "yes":
            num1 = answer
            print("+ \n- \n/ \n* \n ")
            choose=input("Pick an operator: ")
            num2=float(input("Enter a secound Number: "))
            answer=operators[choose](num1,num2)
            print(f"{num1} {choose} {num2} = {answer} ") 
            choice=input(f"Type 'yes' to continue calculating {answer} , or type 'no' to exit: ").lower()
        if choice == "no":
            calculation =False
            print( "\n" *40)
            overall_calculation()

overall_calculation()
    
    
