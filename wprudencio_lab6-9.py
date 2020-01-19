#William Prudencio, Chapter 6 - Lab 9, 8/24/19

''' This program will read from a file called numbers.txt which contains 
intergers. It will then calculate the average for these numbers and
will handle IOError exeptions that are raised when the file is open &
data is read from it, and exeptions raised when the items read are converted 
to numbers. '''

#-----------------Define the main function------------------------------

def main():

    try: 
        numbers = open("numbers.txt", "r") #open numbers.txt
        counter, total = 0, 0 #start the counter and sum of the numbers
    
        for number in numbers: #read the numbers on file
            number = int(number)
            print(number)
            #increase the counter and add to the total
            counter += 1
            total += number

        numbers.close() #close numbers.txt
        print("Average of the numbers read from the file: ", total/counter)

    #Handle exceptions     
    except IOError:
        print("Error - Cannot read file. File may not exist or is named differently.")
    except ValueError:
        print("Error - The file contains non-numeric data.")

#-----------------Call the main function to run the program-----------------
main()
