#William Prudencio, Chapter 10 - lab 1, 10/12/19

''' This program uses the Pet class and its methods to create 
a new pet object based on the data entered by the user and also 
retrieves that data and prints it on screen. '''

#Create the pet class
class Pet:
    #created the init method to set the data attributes
    def __init__(self, name, species, age):
        self.__name = name
        self.__type = species
        self.__age = age

    #method to assign a value to the name field
    def setName(self, name):
        self.__name = name

    #method to assign a value to the animal type field 
    def setAnimalType(self, species):
        self.__type = species
    
    #method to assign a value to the age field 
    def setAge(self, age):
        self.__age = age 
    
    #method to return the value of the name field
    def getName(self):
        return self.__name

    #method to return the value of the animal type field
    def getAnimalType(self):
        return self.__type
    
    #method to return the value of the age field
    def getAge(self):
        return self.__age
    
#Get name, type and age, to create an object of the pet class
name = input("Pet's name: ")
animalType = input("Pet's animal type: ")
age = input("Pet's age: ")

#create pet1
pet1 = Pet(name, animalType, age)

#print pet1 details
print("\n-----Pet Details-----")
print("Name: ", pet1.getName())
print("Animal type: ", pet1.getAnimalType())
print("Age: ", pet1.getAge())
