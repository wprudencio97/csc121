#William Prudencio, Chapter 8 - lab 14, 8/15/19

''' This program reads the contents of the file GasPrices.txt, it then finds
the average price per year and per month, highest and lowest prices per year,
and will generate a txt file which will list the dates and prices sorted from
lowest price to highest and another txt file for highest to lowest. '''

#-------import files needed for the program--------
import testing

#----------Define the main function----------------
def main():
    gasPrices = open("GasPrices.txt", "r")#open file
    listGenerator(gasPrices)
    gasPrices.close() #close file 
    #call the pricePerYear function from the imported file 
    testing.pricePerYear()
    #call the pricePerMonth function from the imported file 
    testing.pricePerMonth()

#-------define the list generator function--------
def listGenerator(gasPrices):
    #create file to store the sorted low to high prices and vice versa
    gasPricesLH = open("GasPricesLH.txt", "w")
    gasPricesHL = open("GasPricesHL.txt", "w")
    #create the two lists for sorting  
    lowToHigh = []
    highToLow = []
    #read the gasPrices file and add spit items to its corresponding list
    for line in gasPrices:
        line = line.rstrip("\n")
        splitLine = line.split(":")
        lowToHigh.append(splitLine)
        highToLow.append(splitLine)

    #add corresponding title to both files   
    gasPricesLH.write("Gas prices sorted from lowest to hightest\n")
    gasPricesHL.write("Gas prices sorted from highest to lowest\n")

    #sort list, create strings, write the data to their files 
    lowToHigh.sort(key=myFunc)
    for i in lowToHigh:
        gasPricesLH.write("Date= " + i[0] + ": Price= $" + i[1] + "\n")
    
    highToLow.sort(reverse=True, key=myFunc)
    for i in highToLow:
        gasPricesHL.write("Date= " + i[0] + ": Price= $" + i[1] + "\n")

    #close both files 
    gasPricesLH.close()
    gasPricesHL.close()

#---------function for sorting by price----------
def myFunc(e):
    return e[1]

#---------call main to run the program-----------
main()