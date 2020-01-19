#William Prudencio, Chapter 7 - lab 10, 9/8/19

''' This program allows the user to enter the name of a team and it then 
displays the times that team has won the world series and the corresponding 
years. The time period range for the results is  1903 - 2018. The program's
input is non-case sensative and will loop until stopped. '''

#------------Define the main function------------------
def main():
    #find initial team 
    searchQuery = input("Please enter a team name or enter stop to cancel the search: ")
    while searchQuery != "stop": #begin loop 
        worldSeriesWinners = open("WorldSeriesWinners.txt", "r") #open file
        #send file and search query to the search function
        search(worldSeriesWinners, searchQuery) 
        worldSeriesWinners.close #close file 
        #find if user wants to search another team or end loop
        searchQuery = input("Please enter a team name or enter stop to cancel the search: ")
    
#-----------Define the search function-----------------
def search(worldSeriesWinners, searchQuery):
    startingYear = 1903 #set first year on file 
    #loop through the file and find search query team
    for winner in worldSeriesWinners:    
        if winner.rstrip("\n") == searchQuery.title():
            print(startingYear,"-", winner.rstrip("\n"))
        startingYear += 1 #increase year for next line

#--------call the main function to run the program-------
main()