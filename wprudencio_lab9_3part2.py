#William Prudencio, Chapter 9 - lab 3 - Part 2, 9/28/19

''' This program will open the Encrypted file from part 1 called
coded_message.txt and display its decrypted content on screen. '''

#import the previous lab to use the coder function
import wprudencio_lab9_3part1 as part1 

#---------Define the main function------------------
def main():
    #open the file 
    codedMessage = open("coded_message.txt", "r")

    #read the file and decrypt the characters
    for character in codedMessage:
        character = character.rstrip("\n")
        print(part1.coder(character))

    #Close the file
    codedMessage.close()

#---------call main to run the program-------------
main()


