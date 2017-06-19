print ("Welcome to the Roll the Dice game!")
roll = input("Do you want to roll the dice or quit? \n r to roll: \n q to quit:")
if roll.lower() == "r":
    import random
    print (random.randint(1, 6)) 
    dice_roll = 1
    total = roll
    print ("You have rolled a total of", dice_roll)
    if roll.lower() == "q":
        quit = input("Are you sure you want to quit:")
if roll.lower() == "d":
    print("hi")
        
        


    
done = False
while not done:
    roll_again = input("Roll again or quit?:")
    if roll_again == "r":
        import random
        print (random.randint(1, 6))
        dice_roll = dice_roll+1
        print ("You have rolled a total of", dice_roll )
    if roll_again == "q":
        q = True
        quit = input("Are you sure you want to quit:")
        if quit == "q":
            done = True
            dice_roll = 0
       
            
            


        
                       
    

       

