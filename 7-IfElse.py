import sys

# The list below represents the ranking of three athletes. John won 1st place, Sen got 2nd, and Lisa the 3rd.
#
# ranking = ['John', 'Sen', 'Lisa']
#
#
#
# Create a program that:
#
# 1. Contains the above list.
#
# 2. Prompts the user to input a rank number.
#
# 3. Returns the person who has the given rank.

# ranking = ['John', 'Sen', 'Lisa']
# rank = int(input("Please provide the rank number from 1 - 3 to see the Athelete: \t"))
# if rank > 3 or rank < 1:
#     print("Please print rank between 1 to 3")
# else:
#     print("The athelete on rank "+ str(rank) +" is:",ranking[rank-1])

# name = input("Please provide the Athelete Name to see Rank:\t")
# print(ranking.index(name)+1)

# Assignment 1 - Checking if a number is Even or Odd

# number = 1
# while number != 0:
#     user_input = input("Please enter a number: (Enter 0 for exiting the program.) \t")   
#     try:
#         number = int(user_input)
#         if number == 0:
#             print("Exiting the program. Bye!!!")
#             break
#         if number%2==0 :
#             print("The given number is even.")
#         else:
#             print("The given number is odd.")
#     except ValueError:            
#         print("Please enter an valid integer.")



# Assignment 2 - Checing if a number if poitive, negative or zero

# user_input = input("Please enter an integer number: ")   
# try:
#     number = int(user_input)
#     if number == 0:
#         print("Entered number is zero.")            
#     elif number < 0:
#         print("The number is negative.")
#     else:
#         print("The number is positive.")
# except ValueError:            
#     print("Please enter a valid integer.")

# Assignment 3 - Grade classification

# user_input = input("Please enter your score (0-100): ")   
# try:
#     number = int(user_input)

#     if number < 0 or  number > 100:
#         print("Please enter the number in the range 0 - 100 only.")
#         sys.exit(1) # Provide a non-zero exit code to indicate an error
#     if number >= 90 and number <=100:
#         print("You have secured grade A.")  
#     elif number >= 80 and number <= 89:
#         print("You have secured grade B.")
#     elif number >=70 and number <= 79:
#         print("You have secured grade C.")    
#     elif number >=60 and number <= 69:
#         print("You have secured grade D.")    
#     elif number <= 59 and number >=0:
#         print("You have secured grade F.")
# except ValueError:            
#     print("Please enter a valid integer.")   



# Assignment 4 - If a entered year is leap year or not

# user_input = input("Please enter a year: ")   
# try:
#     number = int(user_input)

#     if number < 0:
#         print("Please enter the year in the range 0 and above.")
#         sys.exit(1) # Provide a non-zero exit code to indicate an error
#     if number%4 == 0:
#         if number%100 == 0:
#             if number % 400 == 0:
#                 print("Entered year is a leap year.")       
#             else:
#                 print("Entered number is not a leap year.") 
#         else:
#             print("Entered number is a leap year.")        
#     else:
#         print("Entered number is not a leap year")            

# except ValueError:            
#     print("Please enter a valid integer.")   




# Assignment 5: Please specify if a number is within range or not

# user_input = input("Please enter a number between 0 and 100000")   
# try:
#     number = int(user_input)

#     if number < 0 or number > 100000 :
#         print("Please enter the number in the range 0 and 100000.")
#         sys.exit(1) # Provide a non-zero exit code to indicate an error         
#     else:
#         print("Entered number is within range.")            

# except ValueError:            
#     print("Please enter a valid integer.")     

# Assignment 6: BMI Calculator 

user_input_wt = input("Please enter your weight in kilograms")  
user_input_ht = input("Please enter your height in meters")   

try:
    weight = float(user_input_wt)
    height = float(user_input_ht)

    if weight <= 0 or height <=0:
        print("Please enter valid non-zero value for height and weight.")
        sys.exit(1) # Provide a non-zero exit code to indicate an error         
    bmi = weight / (height**2)    
    print("Your BMI is: ", bmi)

    if bmi < 18.5: 
        print("Underweight")
    elif bmi>=18.5 and bmi < 24.9:
        print("Normal weight")
    elif bmi>=25 and bmi < 29.9:
        print("Overweight")  
    else:
        print("Obesity")      
except ValueError:            
    print("Please provide proper value for height and weight.")          