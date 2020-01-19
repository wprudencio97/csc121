#----------------------Define the pricePerYear function------------------
def pricePerYear():
    gasPrices = open("GasPrices.txt", "r")#open the file 

    startingYear = 1993 # set starting year
    counter, total = 0, 0  #declare counter and total
    simpleList = [] #create simple list to store split values
    yearList = [] #to temporarily hold current all current year prices 

    for line in gasPrices: #loop through the file 
        line = line.rstrip("\n")
        splitLine = line.split(":")
        year = splitLine[0][6:10]#read the year
        price = splitLine[1]#read the price 
        #add year and price to the simple list 
        simpleList.append(year +"-"+ price) 

    for i in simpleList: #loop through the simple list
        simpleLine = i.split("-")
        currentYear = int(simpleLine[0])
        currentPrice = float(simpleLine[1])

        #test current if its still the same year
        if currentYear == startingYear:
            counter += 1 #increase counter
            total += currentPrice #add to total
            yearList.append(currentPrice)
        else:
            startingYear += 1 #increase starting year to move on to the next year 
            #print the results for the evaulated year 
            print(startingYear, "| Average: $",round(total/counter, 2), "| Highest: $",max(yearList), "| Lowest: $",min(yearList))
            print("-------------------------------------------------------------")
            counter, total = 0, 0 #Reset the counter and total for the new year
            yearList = [] #reset the year list for the new year
    gasPrices.close()#close the file 



#------------------Define the pricePerMonth function----------------------
def pricePerMonth():
    gasPrices = open("GasPrices.txt", "r")#open the file 

    #create list to store the prices for each month 
    january,february,march,april,may,june,july,august,september,october,november,december = [],[],[],[],[],[],[],[],[],[],[],[]


    for line in gasPrices: #loop through the file 

        line = line.rstrip("\n")
        splitLine = line.split(":")
        month = splitLine[0][0:2]#read the year
        month = int(month)
        price = splitLine[1]#read the price 
        price = float(price)

        #add price to its corresponding month list
        if month == 1:
            january.append(price)
        elif month == 2:
            february.append(price)
        elif month == 3:
            march.append(price)
        elif month == 4:
            april.append(price)
        elif month == 5:
            may.append(price)
        elif month == 6:
            june.append(price)
        elif month == 7:
            july.append(price)
        elif month == 8:
            august.append(price)
        elif month == 9:
            september.append(price)
        elif month == 10:
            october.append(price)
        elif month == 11:
            november.append(price)
        elif month == 12:
            december.append(price)

    #print the results
    print("January - Average cost: $", round(sum(january)/len(january),2))
    print("February - Average cost: $", round(sum(february)/len(february),2))
    print("March - Average cost: $", round(sum(march)/len(march),2))
    print("April - Average cost: $", round(sum(april)/len(april),2))
    print("May - Average cost: $", round(sum(may)/len(may),2))
    print("June - Average cost: $", round(sum(june)/len(june),2))
    print("July - Average cost: $", round(sum(july)/len(july),2))
    print("August - Average cost: $", round(sum(august)/len(august),2))
    print("September - Average cost: $", round(sum(september)/len(september),2))
    print("October - Average cost: $", round(sum(october)/len(october),2))
    print("November - Average cost: $", round(sum(november)/len(november),2))
    print("December - Average cost: $", round(sum(december)/len(december),2))

    gasPrices.close()#close the file 
       