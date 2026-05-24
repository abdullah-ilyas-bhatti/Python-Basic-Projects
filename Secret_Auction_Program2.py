def find_high_bid(bidding_dictionary):

    winner=max(bidding_dictionary, key=bidding_dictionary.get)
    highest_amount=bidding_dictionary[winner]
    print(f"the winner is {winner} with a bid is Rs{highest_amount} ")



bid={}
continue_bidding=True

while continue_bidding:
    name=input("Enter your Name: ")
    price=int(input("Enter your Bid Price Rs"))
    bid[name]=price
    again=input("are there any bidder? Type yes or no ")
    if again == "no":
        continue_bidding=False
        find_high_bid(bid)
    elif again == "yes":
        print("\n"*50)
