print ("Noot Noot Quiz Time")
print ("First Question")
print ("What is the catch phrase of Pengu in the show Pengu: \nPi Pi Pengu \nPe Pe Pengu \nSnoot Snoot\nNoot Noot")
anwser = input("Anwser:")
if anwser.lower() == "noot noot":
    print("Correct")
    anwser = 1
else:
    print("Incorrect, you need to watch more Pengu.")
    anwser = 0
    
print ("Second Question")
anwser1 = input("Are you Ready:")
if anwser1.lower() == "yes":
    print("Pengu Approves")
    anwser1 = 0
else:
    print("Too bad NOOT NOOT.")
    anwser1 = 0


print ("The Real Second Quesiton")
print ("What is Pengu's Favorite Food? \nChicken \nFish \nCookies \nCandy")
anwser2 = input("Pengu's favorite food is:")
if anwser2.lower() == "fish":
    print("You're really nooting this quiz, correct.")
    anwser2 = 1
else:
    print("Incorrect Pengu's a penguin. Try Again!")
    anwser2 = 0

print ("Third question")
print ("If Pengu traveled 120 miles in 10 seconds, What is his speed? \nm/s is not needed just put the number")
anwser3 = input("Pengus speed is:")
if anwser3 == "12":
     print ("Correct")
     anwser3 = 1
else:
    print ("Incorrect, Speed is distance divided by time")
    anwser3 = 0
    
    
    
print ("Question four")
print ("How many Penguins are in Pengu's family? \nA 1\nB 6\nC 4\nD 7")
anwser4 = input("How many family members does Pengu have:")
if anwser4.lower() == "c":
    print("You're a real fan of Pengu eh")
    anwser4 = 1
else:
    print("Incorrect, Go watch some more Pengu.")
    anwser4 = 0



print ("Question five")
print ("What kind of house does Pengu live in? \nbig house\ntreehouse\nigloo\nbox")
anwser5 = input("What kind of house does Pengu live in:")
if anwser5.lower() =="igloo":
    print("NOOT NOOT NOOT NOOT Correct")
    anwser5 = 1
else:
    print("Incorrect, seriously he's an actually penguin.")
    anwser5 = 0
    
    
score = (anwser + anwser2 + anwser3 + anwser4 + anwser5)
a = score / 5 * 100 - .0
print (a,"%")
print (score,"out of 5")
 



    
    
