#William Prudencio, Chapter 10 - lab 9, 10/20/19

''' This program creates a simple ten question trivia game for two players 
based on The Lord of the Rings. Each player will take a turn answering 
questions and once all ten questoions have been answered, the winner will
be decided. The program use a class called question to create the question
objects.'''

#define the question class
class Question:
    #set class attributes----------------------
    def __init__(self,question,answer1,answer2,answer3,answer4,correctAnswer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correctAnswer = correctAnswer
    #set mutators------------------------------
    def setQuestion(self, question):
        self.__question = question
    def setAnswer1(self, answer1):
        self.__answer1 = answer1
    def setAnswer2(self, answer2):
        self.__answer2 = answer2
    def setAnswer3(self, answer3):
        self.__answer3 = answer3
    def setAnswer4(self, answer4):
        self.__answer4 = answer4
    def setCorrectAnswer(self, correctAnswer):
        self.__correctAnswer = correctAnswer
    #set accessors----------------------------
    def getQuestion(self):
        return self.__question
    def getAnswer1(self):
        return self.__answer1
    def getAnswer2(self):
        return self.__answer2
    def getAnswer3(self):
        return self.__answer3
    def getAnswer4(self):
        return self.__answer4
    def getCorrectAnswer(self):
        return self.__correctAnswer

    #method for displaying the questions and answer choices
    def askQuestion(self):
        print("Question: " + self.__question + "\nAnswers: " + \
                "\n1. " + self.__answer1 +\
                "\n2. " + self.__answer2 +\
                "\n3. " + self.__answer3 +\
                "\n4. " + self.__answer4)

#define the function used to play the game 
def playGame(questionBank):
    #store player points for correct answer
    playerOneScore, playerTwoScore = 0, 0

    #loop through the 10 questions
    for i in range(10):
        #check who's turn it is 
        if i % 2 == 0:
            print("\nPlayer 1's turn: ")
            #ask the question
            questionBank[i].askQuestion()
            choice = int(input("Enter the number of your answer choice: "))
            #check the answer and keep score
            if choice == questionBank[i].getCorrectAnswer():
                playerOneScore += 1
        else:
            print("\nPlayer 2's turn: ")
            #ask the question
            questionBank[i].askQuestion()
            choice = int(input("Enter the number of your answer choice: "))
            #check the answer and keep score
            if choice == questionBank[i].getCorrectAnswer():
                playerTwoScore += 1

    #check the scores and determine the winner
    print("\nPlayer 1 score: ", playerOneScore)
    print("Player 2 score: ", playerTwoScore)
    if playerOneScore > playerTwoScore:
        print("PLAYER ONE WINS!!!")
    elif playerTwoScore > playerOneScore:
        print("PLAYER TWO WINS!!!")
    else:
        print("DRAW!!!")

#define the main function
def main():
    #open the file containing the data for the questions
    triviaQuestions = open("trivia-questions.txt", "r")
    #create lists for questionbank, questionlist, answers
    questionBank, questionList = [], []
    answers = [1,3,3,4,3,3,3,2,1,2]

    #read the file and add the items to the list
    for line in triviaQuestions:
        questionList.append(line.rstrip("\n"))

    #close the file 
    triviaQuestions.close()

    # create variables for iterating though the lists 
    i, a = 0, 0
    #iterate through the questions list, create question and it to the question bank
    for j in range(10):
        question = "Question number " + str(j + 1) + ": " +  questionList[i]
        answer1 = questionList[i + 1]
        answer2 = questionList[i + 2]
        answer3 = questionList[i + 3]
        answer4 = questionList[i + 4]
        #create the question object
        question = Question(question, answer1, answer2, answer3, answer4, answers[a])
        #add the question to the question bank list 
        questionBank += [question]
        
        #increase the iterators to move to the appropriate items on the lists 
        a += 1
        i += 5
    
    #send the question bank list to the play game function
    #this make the game play
    playGame(questionBank)


#call the main function to run the program 
main()


#link to original trivia https://www.absurdtrivia.com/quiz/000032/the-lord-of-the-rings/