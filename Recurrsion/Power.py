def power(num,exp):
    if exp == 0:
        return 1
    else:
        return num*power(num,exp-1)
    
print(power(3,9))