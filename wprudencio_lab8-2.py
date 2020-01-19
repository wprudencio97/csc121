#William Prudencio, Chapter 8 - lab 2, 9/14/19

''' This program will ask the user to input a series of single digit 
numbers with nothing separating them. The program will then calculate and 
display sum of all the single digits in the string. '''

#-----------Define the main function----------------
def main():
    #collect the numbers string 
    numbers = input("Please enter a single long number with nothing separating it: ")
    numbersList = list(numbers)#separate each digit into a list
    sumCalculator(numbersList)#send list to the sumCalculator

#--------Define the average calculator function--------
def sumCalculator(numbersList):
    sum = 0 #set the sum variable
    #loop through numbersList, convert i to an int, add i to the sum
    for i in numbersList:
        i = int(i) 
        sum += i
    #print the results 
    print("The sum of every digit for the number you entered is: ", sum)

#---------Call main to run the program-------------
main()