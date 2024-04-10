repeat=True

while repeat:

    while True:
        try:
            length=int(input("Please enter a whole number(max 50):  "))-1
            if length<50:
                break
            else:
                length=int("b")
                
            
        except:
            print("Invalid input, ", end="")


    for i in range (length+1):
        print(" ", end="")
    print("/\\")


    for i in range (length):
        for j in range(length-i):
            print(" ", end="")
                
        print("/",end="")
        for j in range(length-j):
            print("  ", end="")
        print("\\")


    for i in range (length):
        print(" ", end="")
        for j in range(i):
            print(" ", end="")
        print("\\", end="")
            
        for j in range(length -i):
            print("  ", end="")
        print("/",)
            

    for i in range (length+1):
        print(" ", end="")
    print("\\/")
    
    
    while True:
        try:
            again=(input("Would you like to have another go?(y/n):  ")).upper()
            if again==("Y"):
                break
            elif again==("N"):
                repeat=False
                print("goodbye.")
                break
            else:
                print("invalid input.")
                
            
        except:
            print("Invalid input, ", end="")
