#William Prudencio, Chapter 12 -  lab 8, 11/10/19

''' This program uses a recursive function to solve the 
ackermann's function, which tests how well a system 
optimizes its performance of recursion????? '''

#define the main function
def main():
    #get the values for m and n
    mValue = int(input("Enter a value for m: "))
    nValue = int(input("Enter a value for n: "))

    #send the values to the ackermann function
    print(ackermann(mValue, nValue))


#define the ackermann function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1)) 

#call main to run the program
main()