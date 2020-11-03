import time
import sys

intro = "You are about to start your own unique story,\n following 17 year old Rayan from Syrië.\n Just like you, he had a normal life.\n He hang out with friends, went to school and enjoyed his hobby's.\n Until one day, that all changed."
print(intro)
print(" ")

while True:
 error1 = "Please anwser with corresponding letters."
 choice1 = "Would you like to begin the story? \n \n A= yes \n B= no"
 choice2 = "You are walking home from school. Weirdly, the bus does not drive today.\n Suddenly, you hear someone screaming your name.\n It's your friend Emir.\n You stop and ask him what is going on.\n He says you need to come with him.\n \n A= Go with Emir. \n B= Continu walking home."
 choice3 = "Arriving at your friend's house, his mother is nervously walking around the kitchen.\n the two of you stay quiet, until she notices you, sighing of relief.\n Thank god you guys made it. We need to leave right now. \n You refuse, first wanting an explaination. \n It is... complicated, says Ermir's mother. I will tell you when we are underway. \n \n A= Go with them. \n B= Go to your own home."
 choice4 = "during the walk home, you notice how quiet it is. \n almost like everyone is still asleep. \n Suddenly, you hear screaming. It seems to be coming from the direction of your house.\n \n A= Go towards the screaming. \n B= Run the other direction." 
 choice5 = "You go with them. \n 3 weeks pass. You, Emir and his mother have been walking for days now.\n You stop to take a short break and to eat something.\n You don't have much food left, only one piece of bread.\n Who gets the last piece?\n \n A= Keep it yourself.\n B= Give it Emir.\n C= Give it to Emir's mother."
 choice6 = "You start running away.\n You realise maybe you should have come with Emir.\n Still running, you come across a group of people.\n You recognize them. They are your neighbours.\n Confused about what is going on you ask them why they have so much stuff with them.\n They look suprosed to see you. one of them comes to the front of the group.\n She lays a hand on your shoulder and says: Im sorry, but your parents got killed.\n Suddenly, you realize what is going on. you remember the news, your parents having worried arguments, the increasing violence.\n You are in a war.\n \n A= Go with the group.\n B= Search for Emir."
 choice7 = "Quickly walking towards the screaming, you can start hearing voices being drowned out by the screaming.\n You can even start to hear who is screaming. It is your mother.\n You pick up your pace and start to run home.\n Finally home, you see your father laying on the ground, not moving.\n You look up from your father and see your mother being carried away to a truck.\n One of the men starts looking at you, warning the other men."
 choice8 = "You take the last piece for yourself. For days, you offered them part of your food and they always refused, so why would they take it now?\n It's getting dark and you decide to set up camp for the night. \n When you wake up the next day, you hear Emir sobbing.\n Emir's mother died of starvation in her sleep.\n Emir starts to attack you vocally.\n THIS IS ALL YOUR FAULT!, he says.\n \n A= Try to talk it out. \n B= don't do anything and go further alone."
 choice9 = "You give the last piece to Emir. He hasn't had much to eat for the past week.\n It starts to get dark and you decide to set up camp for the night. \n You wake up to the sound of struggle.\n You turn around and see Emir being captured by two man.\n Another man gets out of the truck and starts to walk towards you."
 choice10 = "You give the alst piece to Emir's mother. It starts to get dark and you decide to set up camp for the night. When you wake up the next day you immediately continu the journey."

 print(choice1)
 choice1a = input()
 if choice1a == "a" or choice1a == "A":
     print(choice2)
 elif choice1a == "b" or choice1a == "B":
     set:False
 else:
     print(error1)
 
     
