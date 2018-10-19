#A program to sort places
#Made by Luke Clement
#19/10/18

#Sets up the array to be filled with places
place=[]
#Ready to catch what the first line is
firstLine="Blank"

#Reading the file
try:
    readFile=open("GBplaces.csv","U")
    for line in readFile:
        try:
            #Splitting up each row into its columns
            components=line.split(",")
            #Adding them to the (2D) list [A list of lists]
            place.append([components[0],components[1],int(components[2]),float(components[3]),float(components[4])])
        except:
            #Getting that first line
            firstLine=line
            print("Caught the defining terms, and those would be:"+line)

    #Closing the file
    readFile.close()
except:
    print("File can't be read!")

#Sorting the list depending on population (column 3)
#Key recieves an element from 'place' to sort around. In this case, this is a list.
#Since a list can't be a key, the lambda operator jumps in the help!
#Lambda takes in a argument (in this case a list) and returns (in this case) the second element in that list.
#This gives the program an element to sort around! In this case, population!
place=sorted(place, key = lambda element: element[2])

#Starting to write the sorted file
writeF = open("SortedPlaces.csv","w")

#Write the first line to the file
writeF.write(firstLine)
#Write the rest of the rows
for i in range(len(place)):
    #For every row, write it to the new csv
    writeF.write(place[i][0]+","+place[i][1]+","+str(place[i][2])+","+str(place[i][3])+","+str(place[i][4])+"\n")
#Closing the file
writeF.close()
