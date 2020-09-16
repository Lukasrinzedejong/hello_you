username = input("Hallo ik ben Lukas, hoe heet jij? ")
print("Hallo  " + username)
waarWoon = input("Waar woon jij " + username + "? ")
print ("Ik kom vaak in " + waarWoon + ". Ik heb familie die daar woont. Weet jij iets af van " + waarWoon + "? ")

vraag1 = input(waarWoon + " is a) in Noord Holland b) een klein dorp c) Ik weet het niet ")

if vraag1 == "a" or vraag1 == "A":
    print("Inderdaad! " + waarWoon + " ligt in Noord Holland.")

if vraag1 == "b" or vraag1 == "B":
    print("dat klopt " + waarWoon + " is een erg klein dorp.")

if vraag1 == "c" or vraag1 == "C":
    print("Weet je het niet? Mischien beter opletten bij aardrijkskunde in het vervolg.")

print("                       ")

vraag2 = input("Van deze drie vrijetijds bestedingen, welke past het beste bij jouw? a) Gamen  b) Sporten  c) Muziek spelen ")

if vraag2 == "a" or vraag2 == "A":
    print("Wist je dat gamen een van de meest populaire tijdsbestedingen ter wereld is? ")

if vraag2 == "b" or vraag2 == "B":
    print("Sporten is erg gezond, maar je moet wel uitkijken dat je niet te ver gaat ")

if vraag2 == "c" or vraag2 == "C":
    print("Muziek is bewezen erg ontspannend te zijn ")

print("                           ")

vraag3 = input("Welke richting wil je uit met je opleiding?   a) Mediadevelopment   b) Gamedevelopment  c) Weet ik nog niet  ")

if vraag3 == "a" or vraag3 == "A":
    print("Er is tegenwoordig veel vraag naar Mediadevelopers ")

if vraag3 == "b" or vraag3 == "B":
    print("Gamedeveloper word erg onderschat hoeveel werk het is ")

if vraag3 == "c" or vraag3 == "C":
    print("Er is gelukkig nog tijd genoeg om te kiezen ")
    
