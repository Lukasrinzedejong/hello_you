import time
import sys
while True:
    print(" ")
    print("You are about to start your unique story, do you want to continu?")
    print("yes/no")

    choice1 = input()

    if choice1 == "yes":
        print("This story follows Rayan, a 17 year old boy from syrië.")
        print("You decide his story")
        print(" ")
        print("You have been picked up by your father from school early, but he did not tell why.")
        print("All you know is that your dad looks frightened.")
        print("Do you ask him what is going on?")
        print("yes/no")
        choice2 = input()
        if choice2 == "yes":
            print("You ask your father, and he slowly turns towards you with a worried face.")
            print("He explains that you and your family need to get out of the country.")
            print("You find out your counrty is on the verge of war, and everyone is in danger.")
            print("After a silent drive back home, you decide to start packing your most priced possesions.")
            print(" ")
            print("Your mother walks in, saying it is time to go.")
            print("you ask your mother how they are planning on leaving the country.")
            print("Surely it won't be as easy as just driving across the border.")
            print("she tells you that there are two ways. With a boat, or go with a truck, together with other people trying to escape the country.")
            print("They ask what you would find the best way.")
            print("A) Boat/ B) Truck")
            choice3 = input()

            if choice3 == "A" or choice3 == "a":
                print("your parents listen to your preference and start driving to the boat.")
                print("While driving, you suddenly hear screaming. The first attack started already.")
                print("Your little sister starts crying. Your parents are panicking.")
                print("your parents are debaiting if they should stop the car and start running for the boat.")
                print("are you going to A) get out and walk to the boat, B) stay in the car, or C) say nothing.")
                choice5 = input()
                if choice5 == "A"or choice5 == "a":
                    print("You get out of the car, now on foot to the boat.")
                    print("The boat only is a few kilometers away, but your little sister is already tired.")
                    print("You decide to carry her to the boat.")
                
            elif choice3 == "B" or choice3 == "b":
                print("your parents decide to go with the truck. It is quicker, but more dangerous when you get caught.")
                print("While walking to the truck, what looks to be a middle aged man starts screaming at you and your family.")
                print("you stop to hear what the man is saying, whe nsuddenly you notice. He is holding a firearm.")
                print("He points the weapon at you. What do you do?")
                print("A) Try talking to the man, B) Surrender, C) Run")
                choice7 = input()
                if choice7 == "A" or choice7 == "a":
                    print("you confront the man and you are able to distract him long enough for your father to unarm him.")
                    print("In doing so you father gets hit in the shoulder by a wild shot from the man. Your father still lives, but is severally wounded.")
                    print("Do you A) stop to help your father, B) continu to the truck in hope your father is able to make it with his wound.")
                elif choice7 == "B" or choice7 == "b":
                    print("The man screams something along the lines of NO FORGIVENESS and you get shot.")
                    print("The last thing that goes through your head is your little sister. Hopefully she will make it to a safe place.")
                    
                elif choice7 == "C" or choice7 == "c":
                    print("You run towards cover, hearing bullets zoom past your head.")
                    print("as fast as you are, you are able to catch up to your family, still hearing the man behind you.")
                    print("The man is clearly after you. Do you A) stay with your family, or B) Break away from the group to save the others?")
                
            
            
        elif choice2 == "no":
           print("The drive home is silent.")
           print("When you arrive at your home, your mother runs towards you,saying you need to start packing your stuff.")
           print("while packing your stuff, you hear your parents arguing.")
           print("Your mother is mad at your father for not telling you what is going on.")
        else:
            print("invalid option, restarting story.")
    elif choice1 == "no":
        print("maybe another time.")

    else:
        print("invalid option, restarting story.")
       


    
