#Calculating Kinetic Energy
#Luke Clement
#03/10/18

#Declaring the functions to be used in this program
def calculateKinetic(m, v):

    #Uses mass and velocity to find the energy
    #E=1/2mv^2
    energy = 0.5*m*(v**2)
    #Return the energy
    return energy

#Declaring variables to be used in this program
#Global variables to be used (only the speed of light here)
c = 2.998e8
#In kinetic energy this is mass and velocity
#Ensuring the declared variables are valid
try:
    mass = 3
    velocity = 3
    
    #boolean to check that m and v are valid
    validInputs = mass >= 0 and velocity**2 <= c**2
    
    if(validInputs):
        #Telling the user what the variables are
        #Using scientific notation as it is used more frequently with unusual numbers
        print("The mass is %.2ekg and  the velcoity is %.2ems^-1" %(mass, velocity))
        #Calling the function and telling the user what the energy is
        print("The kinetic energy is therefore %.2eJ" %(calculateKinetic(mass, velocity)))

except:
    print("Invalid inputs! Oh no!")

#Alternatively, user input can be used
#These inputs need to be checked to ensure they are correct
#covering not expected inputs (Strings) using a try/exept
try:
    #Checking to see if the mass is valid
    #Assume invalid to start the loop
    invalidMass=True
    while(invalidMass):
        print("What is the mass of the particle?")
        #Turning the input string to a float by default
        mass = float(input(">>"))
        
        #updates the invalid assumption
        #if it is valid, the program just moves along
        invalidMass = mass < 0
        
        if(invalidMass):
            #Tells the user they input the wrong mass
            print("You can't have negative mass! Try again.")
            
    #The user can input any valid float into this, as velocity can be <0
    #BUT velocity cannot be more than the speed of light, c
    #Same process used to check to see if velocity is correct.
    invalidV=True
    while(invalidV):
        print("What is the velocity of the particle?")
        velocity = float(input(">>"))
        #Checks to see if the user inputted an incorrect value for v
        invalidV = velocity**2 >= c**2
        
        if(invalidV):
            #Informs the user of their mistake
            print("You can't have a velocity greater than light! Try again.")
            

    #Calling the function and telling the user what the energy is
    print("The kinetic energy of the particle is %.2eJ" %(calculateKinetic(mass, velocity)))
except:
    #Letting the user know their inputs were not valid
    print("Invalid input!")

 
