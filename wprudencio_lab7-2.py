#William Prudencio, Chapter 7 - lab 2, 9/7/19

''' This program will generate five lottery numbers ranging from 1 - 69, a
one digit python ball ranging from 1- 69, and a multiplier of a 
single number ranging from 1 - 5. The program will initially ask the 
user how many sets of lottery numbers are to be generated. '''

#------------Define the main function------------------
def main():
    #Get the amount of lottery numbers sets to be generated
    setsToGenerate = int(input("How many sets of lottery numbers would you like? "))

    #Generate the sets
    i = 0
    while i < setsToGenerate:
        lotteryNumbers()
        i += 1

#---------Define the lottery numbers function------------
def lotteryNumbers():
    import random #Import the random number generator
    
    #generate and store lottery numbers
    numList = []  
    for i in range(5):
       numList.append(random.randrange(1,70))

    #Print the results
    print("Lottery Numbers: ", numList)
    print("Python-ball: ", random.randrange(1,70))
    print("Multiplier Number: ", random.randrange(1,6))
    print("-------------------------------------------")

#----------call the main function to run the program------------
main()