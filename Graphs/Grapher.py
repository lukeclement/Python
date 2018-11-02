#A program for visualising the data in GBPlaces.csv
#Luke Clement, 2/10/2018

#Used to view 3D plot
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#Setting up the figure as a 3D projection and setting the size
fig = plt.figure(figsize=(20,20))
#graph is the figure to plot data onto
graph = fig.gca(projection='3d')

#Reading in a csv of the UK coastline courtesy of Ordnance Survey (https://www.ordnancesurvey.co.uk/)
#Slight bit of manipulation on my part to create the csv but the basis image is https://www.ordnancesurvey.co.uk/docs/outline-maps/uk-outline-admin-maps.pdf
#The file used to turn the image into csv can be found on my github: https://github.com/lukeclement/Python/blob/master/Graphs/ImageToCsv.py
readUK=open("UK.csv","r")
latUK=[]
longUK=[]

for line in readUK:
    longlat=line.split(",")
    longUK.append(float(longlat[0]))
    latUK.append(float(longlat[1]))

#Turning collection of coastal data to numpy arrays
UKLat=np.asarray(latUK)
UKLong=np.asarray(longUK)

#Plotting UK coatline at z=0
graph.scatter(UKLat,UKLong,0,zdir='z',s=0.01)

#Now getting data from GBPlaces.csv
PlaceLong=[]
PlaceLat=[]
pop=[]
colours=[]
#Reading file
readFile=open("GBPlaces.csv","r")
for line in readFile:
    try:
      parts=line.split(",")
      
      PlaceLat.append(float(parts[3]))
      PlaceLong.append(float(parts[4]))
      pop.append(float(parts[2]))
      #If above a certain population, label the city
      if(float(parts[2])>=750000):
          #X,Y,Z positions based on where scatter point will be plotted
          graph.text(float(parts[3]),float(parts[4]),float(parts[2])/(10**5)," "+parts[0])
      #And I've got to label Manchester, I'm not a crazy person
      elif(parts[0]=="Manchester"):
          graph.text(float(parts[3]),float(parts[4]),float(parts[2])/(10**5)," "+parts[0])
          
      
      #Show cities and towns in either red or blue
      if(parts[1]=="City"):
          colours.append([0,0,1])
      else:
          colours.append([1,0,0])
    

    except:
        #Data has been found and is starting to be processed (ignores first line)
        print("Got the data!")
       
readFile.close()

#Turning arrays to numpy arrays
PlatTrue=np.asarray(PlaceLat)
PlongTrue=np.asarray(PlaceLong)
popTrue=np.asarray(pop)
col=np.asarray(colours)

#Making axes easier to read by reducing size of numbers
popTrue=popTrue/(10**5)

#Plotting points
graph.scatter(PlatTrue, PlongTrue, popTrue, zdir='z', label='Population of UK cities',c=col)
#Adding seperate colour for towns
graph.scatter(0,0,0,zdir='z', label="Population of UK towns", c=[1,0,0])
#Setting lines to point out where in the UK the cities are
graph.quiver(PlatTrue, PlongTrue, 0, 0, 0, popTrue, arrow_length_ratio=0,color=col)


# Make legend, set axes limits and labels
graph.set_ylim(2, -7)
graph.set_xlim(48.75, 58.75)
graph.set_xlabel('Latitude')
graph.set_ylabel('Longitude')
graph.set_zlabel('Population/10^5')
graph.legend(loc=(0.75,0.75))
#Setting where the graph will view Great Britian from
graph.view_init(elev=40, azim=45*3)
#Saving the figure for outside use
plt.savefig("GBPlaces.png", bbox_inches='tight')
#Letting the user know this
print("Saved Figure as GBPlaces.png")