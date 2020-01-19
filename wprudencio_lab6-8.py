#William Prudencio, Chapter 6 - Lab 8, 8/18/19

''' This program reads the random numbers that were generated into
randomNumbers.txt and will display the following: 1)Count of the 
numbers in the file, 2)Total of the numbers in the file, 3)Average of
the numbers in the file, 4)Largest and smallest number in the file. '''

#-----------------Define the main function---------------------
def main():
    randomNumbers = open("randomNumbers.txt", "r") #open randomNumbers.txt
    readFile(randomNumbers) #send the file to the file reader function
    randomNumbers.close() #close randomNumbers.txt

#-----------------Define the file reader function--------------
def readFile(randomNumbers):

    #start the counter and sum of the numbers
    counter, total = 0, 0
    #declare the variables to store the biggests and smallest numbers
    smallestNumber, biggestNumber = 500, 0

    print("\nNumbers read from file: \n") #print title
    for line in randomNumbers: #read lines on file
        line = int(line.rstrip("\n"))#remove new line character
        print(line) #print the lines 
        #increase the counter and add to the total
        counter += 1
        total += line
        #compare numbers to find biggest/smallest value
        if smallestNumber > line:
            smallestNumber = line
        if biggestNumber < line:
            biggestNumber = line

    #Print the Results 
    print("\nNumbers read from the file: ", counter)
    print("Sum of the numbers read from the file: ", total)
    print("Average of the numbers read from the file: ", total/counter)
    print("Smallest number on the file: ", smallestNumber)
    print("Biggest number on the file: ", biggestNumber)
  
#-----------call the main function to run the program-----------
main()