print("welcome to treasure island")
print(" your mission is to find the treasure")
a=input("u are at a village? do u want to go right  or left")
if a=="left":
    print("u reached a lake ")
    b = input(" swim or wait for the boat")
    if b=="wait":
        print("which door will u choose")
        c = input("red,yellow,blue")
        if c=="red":
            print("you crossed the grand line and found the one piece")
        elif c=="yellow":
            print("u were killed by the Rocks D. Xebec")
        else:
            print("u were killed by the Mariens")

    else:
        print("you were killed by the sea king")

else:
    print("u reached bucky he killed u game over")
