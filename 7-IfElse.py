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

ranking = ['John', 'Sen', 'Lisa']
rank = int(input("Please provide the rank number from 1 - 3 to see the Athelete: \t"))
if rank > 3 or rank < 1:
    print("Please print rank between 1 to 3")
else:
    print("The athelete on rank "+ str(rank) +" is:",ranking[rank-1])

name = input("Please provide the Athelete Name to see Rank:\t")
print(ranking.index(name)+1)




