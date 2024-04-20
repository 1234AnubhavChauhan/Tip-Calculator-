#This is a tip calculator to find the bill to splitted between people .
print("Welcome to the Tip Calculator !!!!")

#Asking for the bill 
bill = float(input("What is the total bill ? "))

# Asking for how much tip you want to give 
tip = int(input("How much tip would you like to give ? 10, 12 or 15 "))

#Total bill is bill plus the tip 
total_bill = bill + tip



#Asking for the number of people to split the amount 
number_of_people = int(input("How many people to split the bill ? "))

#Having some calculations 
final_bill = round(total_bill / number_of_people, 2)


#Finally printing the amount each person has to pay . 
print(f"Each person should pay : {final_bill}")

#Thank You !!!!!!!!!!!!!!!!!!!!!!


























































































