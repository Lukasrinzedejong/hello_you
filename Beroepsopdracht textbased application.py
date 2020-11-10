import time
import sys

while True:

    #intro, keuze voor het spelen
    def intro():      
        print("You are about to start your own unique story,\n following 17 year old Rayan from Syrië.\n Just like you, he had a normal life.\n He hang out with friends, went to school and enjoyed his hobby's.\n Until one day, that all changed.\nWould you like to begin the story? \n \n A= yes \n B= no")   
        intro1 = input()
        if intro1 == "a":
            print("Let's start shall we?")
            choice2()
         
        elif intro1 == "b":
         print("Maybe another time")
         while True:False
        else:
            print("Please anwser with corresponding letters\n")

    #choice2, de grootste keuze in het verhaal     
    def choice2():
        print("You are walking home from school. Weirdly, the bus does not drive today.\n Suddenly, you hear someone screaming your name.\n It's your friend Emir.\n You stop and ask him what is going on.\n He says you need to come with him.\n \n A= Go with Emir. \n B= Continu walking home.")
        choice2a = input()
        if choice2a == "a":
            choice3()
        elif choice2a == "b":
            choice4()
        else:
            print("Please anwser with corresponding letters.\n")
            choice2()

    #choice3, Emir verhaal
    def choice3():
        print("Arriving at your friend's house, his mother is nervously walking around the kitchen.\n the two of you stay quiet, until she notices you, sighing of relief.\n Thank god you guys made it. We need to leave right now. \n You refuse, first wanting an explaination. \n It is... complicated, says Ermir's mother. I will tell you when we are underway. \n \n A= Travel with them. \n B= Go to your own home.")
        choice3a = input()
        if choice3a == "a":
            choice5()
        elif choice3a == "b":
            choice4()
        else:
            print("\n Please anwser using corresponding letters.")
            choice3()

    #choice4, Terug naar huis
    def choice4():
        print("during the walk home, you notice how quiet it is. \n almost like everyone is still asleep. \n Suddenly, you hear screaming. It seems to be coming from the direction of your house.\n \n A= Go towards the screaming. \n B= Run the other direction.")
        choice4a = input()
        if choice4a == "a":
            choice7()
        elif choice4a == "b":
            choice6()
        else:
            print("\n Please anwser using corresponding letters.")
            choice4()

    #Choice5, op de voet het land uit
    def choice5():
        print("You go with them. \n 3 weeks pass. You, Emir and his mother have been walking for days now.\n You stop to take a short break and to eat something.\n You don't have much food left, only one piece of bread.\n Who gets the last piece?\n \n A= Keep it yourself.\n B= Give it Emir.\n C= Give it to Emir's mother.")
        choice5a = input()
        if choice5a == "a":
            choice8()
        elif choice5a == "b":
            choice9()
        elif choice5a == "c":
            choice10()
        else:
            print("\n Please anwser using corresponding letters.")
            choice5()
            
    #choice6, op pad met de groep
    def choice6():
        print("You start running away.\n You realise maybe you should have come with Emir.\n Still running, you come across a group of people.\n You recognize them. They are your neighbours.\n Confused about what is going on you ask them why they have so much stuff with them.\n They look suprosed to see you. one of them comes to the front of the group.\n She lays a hand on your shoulder and says: Im sorry, but your parents got killed.\n Suddenly, you realize what is going on. you remember the news, your parents having worried arguments, the increasing violence.\n You are in a war.\n \n A= Go with the group.\n B= Search for Emir.")
        choice6a = input()
        if choice6a == "a":
            choice11()
        elif choice6a == "b":
            choice12()
        else:
            print("\n Please anwser using corresponding letters.")
            choice6()

    #choice7, naar huis toe
    def choice7():
        print("Quickly walking towards the screaming, you can start hearing voices being drowned out by the screaming.\n You can even start to hear who is screaming. It is your mother.\n You pick up your pace and start to run home.\n Finally home, you see your father laying on the ground, not moving.\n You look up from your father and see your mother being carried away to a truck.\n One of the men starts looking at you, warning the other men.")
        ending1()

    #choice8,
    def choice8():
        print("You take the last piece for yourself. For days, you offered them part of your food and they always refused, so why would they take it now?\n It's getting dark and you decide to set up camp for the night. \n When you wake up the next day, you hear Emir sobbing.\n Emir's mother died of starvation in her sleep.\n Emir starts to attack you vocally.\n THIS IS ALL YOUR FAULT!, he says.\n \n A= Try to talk it out. \n B= don't do anything and go further alone.")
    choice8a = input()
    if choice8a == "a":
        choice18()
    elif choice8a == "b":
        choice19()
    else:
        print("Please use the correct letters.")
        choice8()

    #choice9,
    def choice9():
        print("You give the last piece to Emir. He hasn't had much to eat for the past week.\n It starts to get dark and you decide to set up camp for the night. \n You wake up to the sound of struggle.\n You turn around and see Emir being captured by two man.\n Another man gets out of the truck and starts to walk towards you.")
        ending1()

    #choice10,
    def choice10():
        print("You give the alst piece to Emir's mother. It starts to get dark and you decide to set up camp for the night. When you wake up the next day you immediately continu the journey.")
        choice15()
    
    #choice11,
    def choice11():
        print("You decide to go together with the group .\n They have arranged for a truck to bring them across the border.\n The truck is old and dusty, with barely enough space to fit everyone in.\n You don't know how long you have traveled for, but it feels like weeks.\n you are finally across the border.\n The truck is not able to bring you further.\n You will have to walk to a safe place if you want to survive.")
        ending2()

    #choice12,
    def choice12():
        print("You run to Emir's house, but there is nobody home.\n You see armed men coming towards the house.\n They are yet to spot you. \n A= Go inside the house\n B= Run bak to the group \n")
        choice12a = input()
        if choice12a == "a":
            choice13()
        elif choice12a == "b":
            choice14()
        else:
            print("Please use the correct letters")
            choice12()

    #choice13,
    def choice13():
        print("You enter the house and hide in the kitchen.\n Luckily, the men are just passing by.\n You get up from behin the counter and see a note directed to you.\n It tells you to follow their path, and to get some food from the fridge before leaving.\n You are increadibly tired, and want to get some rest.\n A= Get some rest before leaving\n B= Go immediatly in hopes of catchting up\n")
        choice13a = input()
        if choice13a == "a":
            choice15
        elif choice13a == "b":
            choice15
        else:
            print("Please use the correct letters.")
            choice13()

    #choice14,
    def choice14():
        print("You run back to where you encountered the group but they are gone already.\n You know they wanted to cross the border by truck, and probably already left heading for the truck.\n Suddenly, you see one of the group members running towards you.\n He has come to get you.\n You both head towards the truck, but there are armed men nearby.\n A= quickly get in the truck. B= wait for the men to pass\n")
        choice14a = input()
        if choice14a == "a":
            choice17()
        elif choice14a == "b":
            choice16()
        else:
            print("Please use the correct anwsers.")
            choice14()
    #choice15,
    def choice15():
        print("You get up from your short nap.\n You feel refrehsed, but odd.\n You feel there is something wrong. It is to quiet.\n Emir is gone! \n You decide to look for him. A= Scream his name\n B= Search in quiet\n")
        choice15a = input()
        if choice15a == "a":
            choice18()
        elif choice15a == "b":
            choice19()
        else:
            print("Please use the corresponding letters.")
            choice15()
    #choice16,
    def choice16():
        print("The two of you uickly get into the back of truck, but by doing so you expose the group to the men, causing them to all get captured.")
        ending1()

    #choice17,
    def choice17():
        print("You wait for the men to pass, but they do not pass the truck. They open the back of the truck and you and the group gets captured.")
        ending1()

    #choice18,
    def choice18():
        print("
