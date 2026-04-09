def room1():
    print ("You have entered room 1....")
    print ('''You enter a strange laboratory filled with experiments.
            The exit door is locked, and everything seems… coded''')
    print("You see:\n1.Three paintings on the wall\n2.A paint palette \n3.A locked cabinet\n4.Exit door")
    e=input("Press ENTER to continue:")
    if e=='':
        print('''Each painting has something odd:
                Painting 1 → Sun with 5 rays
                Painting 2 → Tree with 3 apples
                Painting 3 → Hand with 4 fingers

                Above, on wall a quote that says:

                “Count what shouldn’t be.''')
                
        while True:
            
            c=int(input('Enter the correct Code no. to continue:'))
            if c==12:
                print("You've unlocked the cabinet!!")
                break
            else:
                print ("Wrong Code!")
        
        print('''Inside cabinet: a palette with colors:Red, Blue, Yellow
        And  a note that says"Mix the primary ones to get a no. as long as the length"''')
        while  True:
            print("Enter the correct no. recieved from the puzzle:")
            ch_input = input("OR Press enter to receive a clue: ")

            if ch_input == "":
                ch = 0
            else:
                ch = int(ch_input)
            if ch==0:
                print ("THE NEW COLOUR HAS ___ LETTERS")
            elif ch==6:
                print("You've Entered the Final Escape!!\n You move to the exit door to realise it asks for a 3 digit password.")
                p=int(input("ENTER A 3-DIGIT PASSWORD TO OPEN THE DOOR:"))
                if p==126:
                    print("YOU HAVE ESCAPED! GOOD JOB!")
                    break
                else:
                    print("WRONG PASSWORD!")
                    print("HINT:REMEMBER ALL THE NO.S SOLVED SO FAR")

def room2():
    print ("You have entered room 2....")
    print ('''You find yourself trapped inside a mysterious temple filled with symbols, stones, and secrets from the past…''')
    print("You see:\n1.A wall of strange symbols\n2.A pressure plate floor \n3.An old scroll\n4.A sealed stone door")
    e=input("Press ENTER to continue:")
    if e=='':
        print('''Scroll says:
                “Snake = 1, Eye = 2, Sun = 3”
                Wall shows:
                Eye, Sun, Snake, Eye''')
                
        while True:
            
            c=int(input('Enter a 4-digit Code no. to continue:'))
            if c==2312:
                print("Correct!")
                break
            else:
                print ("Wrong Code!")
        
        print('''Suddenly, the tiles light up.\n They follow a certain pattern. Left → Middle → Right → Middle''')
        while  True:
            print("Enter a 4-letter Code to activate the door:")
            ch=input("")
            if ch=='LMRM'or ch=='lmrm':
                print('''You've Entered the Final Escape!!\n You move to the exit door. There are 3 statues kept beside the door.\nThree statues:
                        Small (1 unit)
                        Medium (2 units)
                        Large (3 units)
                        
                        The door asks a Alphanumeric password having 6 characters and also has "LN" marked to it:''')
                p=input("ENTER  THE CODE  TO OPEN THE DOOR:")
                if p=='S1M2L3'or p=='s1m2l3':
                    print("YOU HAVE ESCAPED! GOOD JOB!")
                    break
                else:
                    print("WRONG PASSWORD!")
                    print("HINT:follow the letter-no.-letter-no.... pattern (LN)")
                 
            else:
                print("Wrong Code! try again!")
                

while True:
    print ("WELCOME TO THE ESCAPE ROOM GAME")
    ch_input=int(input("ROOM1: Artist's Room\nROOM2:Temple\nEnter 1 or 2 choose room or press enter 0 to exit game:"))
    if ch_input == "":
        ch = 0
    else:
        ch = int(ch_input)
    if ch==1:
        room1()
    elif ch==2:
        room2()
    elif ch==0:
        break
    else:
        print("Invalid room!")
