#Calculating Kinetic Energy
#Luke Clement
#03/10/18

#Declaring the functions to be used in this program
def calculateKinetic(mass, velocity):

    #Uses mass and velocity to find the energy
    #E=1/2mv^2
    energy=0.5*mass*(velocity**2)
    #Return the energy
    return energy

#Declaring variables to be used in this program
#In kinetic energy this is mass and velocity
mass=3
velocity=3

#Telling the user what the variables are
#Using scientific notation as it is used more frequently with unusual numbers
print("The mass is %.2ekg and  the velcoity is %.2ems^-1" %(mass,velocity))
#Calling the function and telling the user what the energy is
print("The kinetic energy is therefore %.2eJ" %(calculateKinetic(mass,velocity)))

#Alternatively, user input can be used
#covering not expected inputs using a try/exept
try:
    #Checking to see if the mass is valid
    #Assume invalid to start the loop
    invalidMass=True
    while(invalidMass):
        
        print("What is the mass of the particle?")
        #Turning the input string to a float
        mass=float(input(">>"))
        
        #updates the invalid assumption
        #if it is valid, the program just moves along
        invalidMass=mass<0

        if(invalidMass):
            #Tells the user they input the wrong mass
            print("You can't have negative mass! Try again.")
            
    #The user can input any valid float into this, as velocity can be <0
    print("What is the velocity of the particle?")
    velocity=float(input(">>"))

    #Calling the function and telling the user what the energy is
    print("The kinetic energy of the particle is %.2eJ" %(calculateKinetic(mass,velocity)))
except:
    #Letting the user know their inputs were not valid
    print("Invalid input!")

 