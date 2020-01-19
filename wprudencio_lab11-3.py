#William Prudencio, Chapter 11 - lab 3, 11/5/19

''' This program uses a class called person and a subclass of 
person called customer. The program demostrates an instance of the 
customer class using predifined details. '''

#------------Define the Person class------------
class Person:
    #Set the class attrivutes 
    def __init__(self, name, address, phoneNumber):
        self.__name = name
        self.__address =  address
        self.__phoneNumber = phoneNumber 
    
    #set the mutators 
    def setCustomerName(self, name):
        self.__name = name 
    def setCustomerAddress(self, address):
        self.__address =  address
    def setCustomerPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    #set the accessors
    def getCustomerName(self):
        return self.__name
    def getCustomerAddress(self):
        return self.__address
    def getCustomerPhoneNumber(self):
        return self.__phoneNumber

#-----------define the customer subclass----------
class Customer(Person):
    #define the class attrivutes
    def __init__(self, name, address, phoneNumber, customerNumber, mailingList):
        self.__customerNumber = customerNumber
        self.__mailingList = mailingList
        Person.__init__(self, name, address, phoneNumber)
    
    #set the mutators 
    def setCustomerNumber(self, customerNumber):
        self.__customerNumber = customerNumber
    def setMailingList(self, mailingList):
        self.__mailingList =  mailingList

    #set the accessors
    def getCustomerNumber(self):
        return self.__customerNumber
    def getMailingList(self):
        if self.__customerNumber == True:
            return "On mailing list!"
        else:
            return "Not on mailing list!"

#-----------define main-----------------
def main():
    #create a customer object 
    Customer1 = Customer("Thor", "Asgard", "999-000-9999", 117, False ) 

    #print the customer details 
    print("\n--------Customer Information-------")
    print("Name: ", Customer1.getCustomerName())
    print("Address: ", Customer1.getCustomerAddress())
    print("Phone Number: ", Customer1.getCustomerPhoneNumber())
    print("Customer Number: ", Customer1.getCustomerNumber())
    print("Mailing list status: ", Customer1.getMailingList().title())

#call main to run the program
main()