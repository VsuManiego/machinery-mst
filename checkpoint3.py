# TITLE:          Checkpoint_2
# PROGRAMMER 1:   Daniel Joseph N. Sano
# PROGRAMMER 2:   Jhuniel Gumba Munez
# PROGRAMMER 3:   Jianne G. Tajanlangit



mymachineinventory = {}                                                                               
print("Welcome Engineer!")
print("You would like to have a better storage system for your mechanical knowledge.")
print("You have made the right choice!")

import cv2

filepath = ("C:/media/mech.jpg")
image = cv2.imread(filepath)
cv2.imshow("OpenCV Image Reading", image)

cv2.waitKey(3000) 

print("Let's begin with your name")

a = str(input("Name of Engineer: "))
print("Hello Engineer ", a)
print("You want to add new set of machineries?")                             
print("Let's start?")

while (True):                                                                  
    myitem = input("Input new machineries. " "If you're finish, type 'Orayt': ") 
    if myitem == "Orayt":                                                       
        print("Information successfully added!")                                  
        print("Thanks for the information!")
        break
    inputs = input("What type of machinery is this: ")                                            
    desc = input("What's the use of it: ")                                       
    link = input ("Add links: ")
    mymachineinventory[(myitem),(inputs),(desc)] = (link)  
        
    print(f'New set of inventories {mymachineinventory}.')

