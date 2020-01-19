#William Prudencio, Chapter 8 - lab 5, 9/14/19

''' This program will ask the user to enter a telephone number in the format
of xxx-xxx-xxxx which can also contain alphabetic letters. The program will
then translate any alphabettic letters to their numeric equivalent 
and display the telephone number. '''

#---------define the main function---------------
def main():
    #get the telephone number
    telephoneNumber = input("\nPlease enter a telephone number below: \n1. Use the format XXX-XXX-XXXX \n2. Can contain alphabetical letters\n")
    #send the telephone to the splitter function
    splitter(telephoneNumber)

#--------define the splitter funcion---------------     
def splitter(telephoneNumber):
    digits = telephoneNumber.split("-")#split the number
    translatedNumber = "" #create variable for translatedNumber
    for i in digits: #check for letters
        if i.isdigit():
            #if no letters, concatenate to translatedNumber
            translatedNumber = translatedNumber + i + "-"
        else:
            #if it contains letters, further split
            digitList = list(i)
            newDigits = "" #create variable for new digits 
            #check further split digits 
            for e in digitList:
                if e.isdigit():
                    #if no letters, concatenate to newDigits
                    newDigits = newDigits + "e"
                else:
                    #send letter to the tranlator function to get its number equivalent 
                    #concatenate to newDigits
                    newDigits = newDigits + translator(e.capitalize())

            translatedNumber = translatedNumber + newDigits + "-"

    print("\nThe telephone number you entered is:",translatedNumber[:-1:])

#---------define the translator function-----------
def translator(digit):
    number = 0 #define number variable

    #find number equivalent for received letter
    if digit == "A" or digit == "B" or digit == "C":
        number = "2"
    elif digit == "D" or digit == "E" or digit == "F":
        number = "3"
    elif digit == "G" or digit == "H" or digit == "I":
        number = "4"
    elif digit == "J" or digit == "K" or digit == "L":
        number = "5"
    elif digit == "M" or digit == "N" or digit == "O":
        number = "6"
    elif digit == "P" or digit == "Q" or digit == "R" or digit == "S":
        number = "7"
    elif digit == "T" or digit == "U" or digit == "V":
        number = "8"
    elif digit == "W" or digit == "X" or digit == "Y" or digit == "Z":
        number = "9"

    return  number #return the number equivalent 

#--------call main to run the program-----------
main()