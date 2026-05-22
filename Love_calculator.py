name1=input("Enter  your Name: ")
name2=input("Enter your Patner Name: ")
def calculate_love_score(name1 , name2):
    combined_name= (name1 + name2).lower()
    t = combined_name.count("t")
    r = combined_name.count("r")
    u = combined_name.count("u")
    e = combined_name.count("e")
    total_true = t + r + u + e
    
    l = combined_name.count("l")
    o = combined_name.count("o")
    v = combined_name.count("v")
    e = combined_name.count("e")
    total_love = l + o + v + e
    
    grand_total = str(total_true) + str (total_love)
    print(grand_total)

calculate_love_score( name1 , name2)
