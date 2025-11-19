import random
computer= random.choice ([1,-1,0])
your= input("enter you choice :").strip().lower()
youDict={"s" : 1 , "w" : -1 , "g" : 0 }
you=youDict[your]
reverseDict={1:"snake", -1: "water" , 0: "gun"}
print (f"you choice {reverseDict[you]}\n computer choice {reverseDict[computer]} ")
if (computer==you) :
    print("it is draw")

else:
    
    if((computer-you)==-1 or (computer-you) == 2):
        print("you loss")

    else:
        print("you win !")

