import random
data=[ 
    {
        "name":" ",
        "followers":" ",
        "description":" ",
        "country":" ",
    },
    
    ]
print(logo)
score=0
game_continue=True
profile_b=random.choice(data)

while  game_continue:  
    def format(profile):
        a_name=profile["name"]
        a_description=profile["description"]
        a_country=profile["country"]
        return f"{a_name},a {a_description}, in {a_country}"
        
    def compare(userguess, afollowers, bfollowers):
        if afollowers > bfollowers:
            return userguess == "a"
        else:
            return userguess == "b"
        
    profile_a=profile_b
    profile_b=random.choice(data)
    if profile_a == profile_b:
        profile_b=random.choice(data)
        
    
        
    print(f"Compare A: {format(profile_a)}")
    print(vs)
    print(f"AgainstB: {format(profile_b)}")
    guess=input("who has more folowers Type 'A' and 'B' ? ").lower()
    print("\n"*20)
    print(logo)
    
  
    
    a_followers=profile_a["followers"]
    b_followers=profile_b["followers"]
    
    
    correct=compare(guess,a_followers,b_followers)
    if correct == True:
        score+=1
        print(f"oh my yes, You are right your score is {score}")
    else:
        game_continue=False
        print(f"sorry You lose, Final score is {score}")
        
    
    
    
    
    
    
    
    
    
    
    
    
