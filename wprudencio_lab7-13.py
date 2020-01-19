#William Prudencio, Chapter 7 - lab 13, 9/10/19

''' This program will allow the user to ask a yes or no question.
The user will then receive an answer that is randomly selected 
using a random number generator and the attached file of
8_ball_responses.txt '''

#--------------Define the main function------------- 
def main():   
    responses = fileReader() #collect list from function
    magicQuestion(responses) #answer questions 

#-------Find out if user has questions and answer them--------
def magicQuestion(responses):
    question = "yes" #initial question to begin loop
    
    while question != "no": 
        ask = input("What would you like to know? ")
        answer = magicAnswer(responses)#get a random answer
        print(answer)#print the random answer
        #find out the user has another question, if not, loop will end
        question = input("\nWould you like to ask another question: yes or no... ")

#-------------Random answer function------------------
def magicAnswer(responses): 
    import random #import the random number generator
    return random.choice(responses)#return a random answer 
            
#----------Define the file reader function-------------     
def fileReader():
    responseList = [] #create list to store responses from file
    file_object = open("8_ball_responses.txt", "r")   #open the file
    
    for line in file_object: #Read the lines 
        line = line.rstrip("\n")#remove the line break
        responseList.append(line) #add the lines to the list
        
    file_object.close() #Close the file   
    return responseList   

#---------Call the main function to run program----------
main() 
