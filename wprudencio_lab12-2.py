#William Prudencio, Chapter 12 - lab 2, 11/10/19

''' This program uses a recursive function to find the value of
x multiplied by the value of y. In the recursive function, if the else statement 
is triggered, the function decreases the x value by 1 and calls itself 
again and again, until the x value is equal to 1. The y value gets 
added to itself on each iteration. Basically this works as repeated 
addition to find the results of the multiplication equation, so for
example 3 * 7 would be 7 + 7 + 7  '''

#define the main function
def main():
    print("------------------------------")
    #get the x and y values from the user
    xValue = int(input("Enter the value of x: "))
    yValue = int(input("Enter the value of y: "))

    #call the repeated addition function and print the results
    print("\nThe result of", xValue, "x", yValue, "is", repeatedAddition(xValue, yValue))
    print("------------------------------")

#define the repeated addition funtion
def repeatedAddition(x, y):
    if x == 1:
        return y
    else:
        return y + repeatedAddition(x - 1, y)


#call main to run the program
main()
    