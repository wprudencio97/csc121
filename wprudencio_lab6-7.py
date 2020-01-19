#William Prudencio, Chapter 6 - Lab 7, 8/17/19

''' This program writes a series of random numbers to a file named randomNumbers.txt
The random numbers generated range from 1 through 500 and the user specifies how 
many numbers are to be generated '''

#-------------Define the main function-------------------------
def main():
    #Get the amount of random numbers to be generated.
    numsToGenerate = int(input("How many random numbers would you like to generate? "))

    #Send the amount to the number genetator function.
    numGenerator(numsToGenerate)

#------------Define the number generator function--------------
def numGenerator(numsToGenerate):
    import random #Import the random number generator

    #Create the randomNumbers.txt file 
    randomNumbers = open("randomNumbers.txt", "w")

    #Generate and save the numbers to randomNumbers.txt
    i = 0
    while i < numsToGenerate:
        nums = str(random.randrange(0, 501))
        randomNumbers.write(nums + "\n")
        i += 1

    #Close the randomNumbers.txt file
    randomNumbers.close()

#-----------Call the main function to run the program----------
main()
