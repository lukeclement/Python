#A program that uses PV=RT
#Made by Luke Clement
#12/10/18

#Function to find Pressure/Volume- Can be used for either
def findPV(a,t):
    #P=RT/V
    try:
        #Verifing that user inputs are okay to use
        A,T = verify(a,t)
        return R*T/A
    except:
        return None


#Function to find Temperature
def findT(p,v):
    try:
        #Verifing that user inputs are okay to use
        P,V = verify(p,v)
        return P*V/R
    except:
        return None

#Verification process for user input
def verify(a,b):
    try:
        #Casting inputs into floats
        A = float(a)
        B = float(b)
        #Checking to see that the floats are non-zero and above zero
        if(A > 0 and B > 0):
            #Returning the now validated floats
            return A,B
        else:
            print("Negative values not allowed!")
            return None,None
    except:
        #Only used if values are not floats
        print("Only numbers allowed!")
        return None,None



#Function that asks the value to be calculated
def request():
    #Setting output varible to 0
    #If it stays at 0, then an invalid input has been typed
    output = 0
    print("Which value would you like to input?")
    print("Pressure    [P]")
    print("Volume      [V]")
    print("Temperature [T]")
    q = input(">>")
    #Volume is set to 1, Pressure to 2, and Temperature to 3
    if(q == "V" or q == "v"):
        output = 1
    elif(q == "P" or q == "p"):
        output = 2
    elif(q == "T" or q == "t"):
        output = 3
    else:
        print("Invalid input!")

    return output

#Setting global variables
R = 8.315
#Starting the while loop in motion
calculating = True
while(calculating):
    #V is 1, P is 2, T is 3
    #Setting value to 0
    value = 0
    #Seeing if values are set
    pSet = 0
    tSet = 0
    vSet = 0
    #Setting starting values to nonexistant
    T = None
    V = None
    P = None
    #Starting the loop that asks for the inputs
    #Once two DIFFERENT variables have been input, the program moves on
    while(pSet + tSet + vSet < 2):
        
        while(value == 0):
            #Asking the user which input they want
            value = request()
        #Asking the user for inputs
        if(value == 1):
            #Asking the user for inputs and ensuring they are valid
            while(not V):
                print("What is the Volume? [m^3]")
                V,a = verify(input(">>"),1)
            
            #Setting the V makes vSet 1, meaning V is set (and can be reset)
            vSet = 1
        elif(value == 2):
            while(not P):
                print("What is the Pressure? [Pa]")
                P,a = verify(input(">>"),1)
                
            pSet = 1
        else:
            while(not T):
                
                print("What is the Temperature? [K]")
                T = float(input(">>"))
                
            tSet = 1
        #Resetting value (to allow for while loop to go)
        value = 0
    #From what wasn't set, the unknown can be calculated!
    if(pSet == 0):
        P = findPV(V,T)
    elif(vSet == 0):
        V = findPV(P,T)
    else:
        T = findT(P,V)
    #Letting the user know what all the variables are!
    print("The pressure is %.2ePa, where the Volume is %.2em^3 and Temperature is %.2eK for 1 mole of substance" %(P,V,T))

    #Asking the user to do another calculation
    print("Would you like to do another calculation? (y/n)")
    ask = input(">>")
    #Will loop if the condition below is true
    calculating = ask == "y" or ask == "Y"
    
