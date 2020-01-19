#define the question class
class Question:
    #set class attributes
    def __init__(self,question,answer1,answer2,answer3,answer4,correctAnswer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correctAnswer = correctAnswer
    #set mutators and accessors 
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


triviaQuestions = open("trivia-questions.txt", "r")
qList = []
answers = [1,3,3,4,3,3,3,2,1,2]

for line in triviaQuestions:
    qList.append(line.rstrip("\n"))

triviaQuestions.close()

question1 = Question(qList[0],qList[1],qList[2],qList[3],qList[4],answers[0])
question2 = Question(qList[5],qList[6],qList[7],qList[8],qList[9],answers[1])
question2 = Question(qList[10],qList[11],qList[12],qList[13],qList[14],answers[2])
question3 = Question(qList[15],qList[16],qList[17],qList[17],qList[18],answers[3])

numQuestions = 4

while numQuestions != 0:
    if numQuestions % 2 == 0:
        print("Player 1's turn: ")
        
    else:
        print("Player 2's turn: ")
    
    numQuestions -= 1

#https://www.slader.com/textbook/9780134444321-starting-out-with-python-4th-edition/549/programming-exercises/9/