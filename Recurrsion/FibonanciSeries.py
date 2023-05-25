def fibonnaci(n):
    if n in [0,1]:
        return n
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

n = int(input("Please enter number till you want Fibonnaci series:"))
counter = 0
while counter <= n:
    print(fibonnaci(counter))
    counter = counter+1