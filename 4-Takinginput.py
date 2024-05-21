name = input("Enter your name:")
print("Hello", name)

Hours = input("Enter Hours: ")
Rate = input("Enter Rate/Hour: ")

print("Pay:",float(Hours)*float(Rate))


print("Lising value till the integer number taken from the input")
try:
    x = int(input("Please enter an integer value between 1 to 100: "))
    if 1 <= x <= 100:
        for i in range(1, x):
            print(i)
    else:
        print("Entered value is not within the range of 1 to 100.")
except ValueError:
    print("Entered value is not an integer.")