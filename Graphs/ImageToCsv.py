from PIL import Image
import numpy as np
long=[]
lat=[]

test=[]
print("Opening OS image...")
img=Image.open("images.png")
test=np.asarray(img)
print("Total # of points to assess: "+str(len(test)*len(test[0])))
for i in range(0,len(test)):
    for j in range(0,len(test[0])):
        if(test[i][j][0]<128):
            lat.append(i)
            long.append(j)
    if(i==len(test)/2):
        print("50% done!")
    
    
    
print("Complete! Making into numpy arrays...")
pureLat=np.asarray(lat)
pureLong=np.asarray(long)
print("All good! Mapping onto true coordanates...")
longM=(2.361786-0.123166)/(1560-1118)
longC=-0.123166-longM*1560

latM=1/((2417-2322)/(51.504331-51.810827))
latC=51.504331-latM*2417

pureLong=longM*pureLong+longC
pureLat=latM*pureLat+latC

writer=open("UK.csv","w")
for i in range(len(lat)):
    writer.write(str(pureLong[i])+","+str(pureLat[i])+"\n")
writer.close()