#William Prudencio, Chapter 11 - lab 1, 10/26/19

''' This program creates employee class and a subclass of it called 
production worker. The program creates an object of the production worker
class based on user input and it then print's those employee details. '''

#-------------------define the employee class-------------------
class Employee:
    #set the class attrivutes--------------------------
    def __init__(self, employeeName, employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber
    #set mutators-------------------------------------
    def setEmployeeName(self, employeeName):
        self.__employeeName = employeeName
    def setEmployeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber
    #set accessors------------------------------------
    def getEmployeeName(self):
        return self.__employeeName
    def getEmployeeNumber(self):
        return self.__employeeNumber
    
#-----------define the production worker subclass--------------
class ProductionWorker(Employee):
    #set the class attributes-------------------------
    def __init__(self, employeeName, employeeNumber, shiftNumber, payRate):
        self.__shift = shiftNumber
        self.__payrate = payRate
        Employee.__init__(self, employeeName, employeeNumber)
    
    #set the mutators----------------------------------
    def setShiftNumber(self, shiftNumber):
        self.__shift = shiftNumber
    def setPayRate(self, payRate):
        self.__payrate = payRate
    
    #set accessors------------------------------------
    def getShiftNumber(self):
        if self.__shift == 1:
            return "Day"
        else:
            return "Night"
    def getPayRate(self):
        return self.__payrate

#----------------define the main function----------------------\
def main():
    #get employee details from the user
    name = input("Employee Name: ")
    number = input("Employee Number: ")
    shift = int(input("Shift Number: "))
    pay = input("Hourly pay rate: ")

    #create a production worker from the information provided 
    worker1 = ProductionWorker(name, number, shift, pay)

    #print the worker 1 information
    print("\n-------Employee Details-------")
    print("\nEmployee Name: ", worker1.getEmployeeName())
    print("Employee Number: ", worker1.getEmployeeNumber())
    print("Shift: ", worker1.getShiftNumber().title())
    print("Pay rate: $", worker1.getPayRate())

#call main to run the program
main()