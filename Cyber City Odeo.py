"""This is your choose your own adventure game for all to play"""
"""This code will all about Cyber City Odeo 808 in some ways"""
#Start with a simple print command
msg1 = f"BEEP BEEP BEEP"
msg2 = f"The alarm is on, let the endless cycle continue"
msg3 = f"Time to wake up for another of bounty hunting"
print(msg1)
print(msg2)
print(msg3)

#Here is where the game will begin
#Write an input for the yes/no, remember to add lower and strip
answer = input("Would you like to continue? (yes/no) ")
if answer.lower().strip() == "yes":
    #Here is where the game starts if you select yes
    print("You woke up from your bed, you had flashes of the world your mother used to live", '\n')
    print("The world has changed so much than what your mother used to know. You miss here", '\n')

    #Here is where the choose your own adventure starts
    #Note: input key, you need to do that to ask the questions for the text based player
    answer = input ("There's some items next to your bed. Would like the inspect or no? ")
    if answer == "inspect":
        print("You inspect the items: a gun, medicine capsule, badge, and a necklace", '\n')

        answer = input("You want to make sure what you see. Your unsure to which to check first. Would you check the gun/medicine/badge/necklace? ")
        #This is all 'if' satements for the items
        if answer == "gun":
            print("You grab your gun. Its a Komotsu model revolver.", '\n')
            print("Guess many weapon manufactures loved blade runner a lot they made this a reality, though its a good weapon to kill any target", '\n')
            print("You then put it back on the where you grabbed it.", '\n')

            #NOTE: You need to write an 'input' to write the questions for the decision making
            answer = input("Best start the day, would you like to start the day? (yes/no)")
            if answer == "yes":
                print("You then got from bed. The night job are cruel", '\n')
                print("You then proceed to take all your items. You put on your jacket, activate your bionic-arm, and begin the day", '\n')
                print("Let the hunting begin", '\n')

                msg4 = F"          Time: 12:00 pm, day: 20th, month: December, year: 3020, City: Oedo          "
                print(msg4, '\n')
                print("")
                answer = input("You reached the C.C.O police station, best go inside to talk to the collar man himself. You want to in or look around outside? (enter/explore) ", '\n')

            else:
                print("You proceed to stay in bed and get extra sleep.", '\n')
                print("Time: 11:30 pm", '\n')




        elif answer == "medicine":
            print("There pills for PTSD and sleep paralisys. The war tends to break man or woman in many ways.", '\n')
            #This continues with the medicine
            answer = input ("Would like to take your meds or no? ")
            if answer == "meds":
                print("You down two pills just in case the pains comes at any time", '\n')
                print("Besides, its you need to also take it for your Bio-arm you got after your service 7 years ago.", '\n')
            else:
                print("You decide to not take your meds.", '\n')
                print("This will affect you, be aware of the affects", '\n')
                #Let the day begin
                answer = input("Best start the day, would you like to start the day? (yes/no)")



        elif answer == "badge":
            print("You grab your badge given to you after the State gave you a deal.", '\n')
            print("Thank god, the government knew they need criminals to kill other criminals", '\n')
            #Remember what you wrote before for note(s)
            answer = input("Do you want to open open your badge? (yes/no) ")
            if answer == "yes":
                print("You proceed to open your badge. A hologram display shines, and shows your identification and position", '\n')
                name = input("What is your full name is? ")
                num = input("What is your prisoner number? ")
                age = int(input("What is your age? "))
                if age < 22:
                    print("You see your full idefication")
                    id1 = [name]
                    id2 = [num]
                    id3 = [age]
                    print(id1)
                    print(id2)
                    print(id3)
                    uprint("Occupation: Bounty Hunter of Oedo"), '\n'
                    #Let's start the day
                else:
                    print("You see your full idefication")
                    id1 = [name]
                    id2 = [num]
                    id3 = [age]
                    print(id1)
                    print(id2)
                    print(id3)
                    print("Occupation: Bounty Hunter of Oedo")
                    print("Restriction: Not allowed near knifes or blades"), '\n'
                    #Let's start the day
                    answer = input("Best start the day, would you like to start the day? ")


        elif answer == "necklace":
            print("You pick up the necklace, its old and warned out."), '\n'
            print("The necklace is a cresent moon. It was given by your mother as a sign of luck and guidence. Where ever the cesent moon shines bright it will light towards your purpose."), '\n'
            
            #Let the day start
            answer = input("Best start the day, would you like to start the day? ")














else:
    print("Well the game is over, guess you didn't want to explore this cyberpunk world.")

