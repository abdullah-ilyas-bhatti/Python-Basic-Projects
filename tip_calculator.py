print("Welcome to the Tip Calculator")
bill=float(input("what's the total bill ? "))
tip=int(input("what's Percentage you would like to give ex: 10% , 20% , 30% ? "))
people=int(input("how many people to split the bill ? "))
final_tip= tip / 100 * bill
total_bill= bill + final_tip
per_person= total_bill / people
final_output=round(per_person,2)
print(f"so per person should pay the {final_output}" )
