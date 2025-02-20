#Rock beats scissors
#Scissors beats paper 
#Paper beats rock


import random 

while True:
    print("\n")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    
    selection = int(input("Enter Throw: "))
    if (selection == 1):
         player_throw = "Rock"
    elif (selection == 2):
         player_throw = "Paper"
    else:
         player_throw = "Scisors"
    
    
    print ("\n")
    print("Player throws", player_throw)

    throws = ["Rock", "Paper", "Scissors"] 
    ai_throws = random.choice(throws) 
    
    print("AI throws", ai_throws)
    if (player_throw == ai_throws):
        print("Tie Game!")

    elif (player_throw == "Rock"):
        if (ai_throws == "Paper"):
             print("AI wins!")
        elif (ai_throws == "Scissors"):
            print("Player Wins!")
    elif (player_throw == "Paper"):
        if (ai_throws == "Scissors"):
             print("AI wins!")
        elif (ai_throws == "Rock"):
            print("Player Wins!")     
    elif  (player_throw == "Scissors"):
        if (ai_throws == "Rock"):
             print("AI wins!")
        elif (ai_throws == "Paper"):
            print("Player Wins!")           
            
            
    print("\n")
    print("1) Play again")
    print("2) Quit")
    selection = int(input("Enter choice:"))

    if (selection == 2):
        break
    