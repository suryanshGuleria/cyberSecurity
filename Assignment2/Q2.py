
def findrange(low,high,n):
    if(n < low):
        print("The Number is not in range")
    elif( n > high):
        print("The Number is not in range")
    else:
        print("The Number is in range")

low=int(input("Enter the starting limit"))
high=int(input("Enter the ending limit"))
n=int(input("Enter the no. to be checked"))
findrange(low,high,n)
