#William Prudencio, Chapter 9 - lab 3 - Part 1, 9/21/19

''' This program will open and read message.txt, and it will write the encrypted 
morse code version to coded_message.txt '''    


#----------Declare the main function--------------
def main():

    #Open the txt files and create the file for the coded message
    message = open("message.txt","r")
    codedMessage = open("coded_message.txt","w")
    
    #iterate message.txt, 
    for line in message:
        for i in range(len(line)):
            #use the coder function to encrypt each character
            #write the encrypted characters to the coded message file
            codedMessage.write(coder(line[i]) + "\n")

    #close the txt files
    message.close()
    codedMessage.close()


#---------Declare decoder function-----------------
def coder(character):
    #change received character to uppercase 
    character = character.upper()
    codedCharacter = ""

    #morse code dictionary
    morseCode = { "A":".-", "B":"-...", "C":"-.-.", "D":"-..", 
    "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---",
    "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", 
    "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", 
    "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "0":"-----","1":".----", 
    "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....",
    "7":"--...", "8":"---..", "9":"----." }

    #look for the character 
    if character in morseCode:
        codedCharacter = morseCode[character]
    else:
        for key in morseCode:   
            if morseCode[key] == character:
                codedCharacter = key

    #return found character
    return codedCharacter

main()