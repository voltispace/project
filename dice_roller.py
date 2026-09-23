import random
# def roll_dice():
attempts = 5

print("=" *22)
print(f"\033[105mWELCOME TO DICE ROLLER\033[0m")
print("=" *22)
    
    
while True:
    
            try:  
               choice = input("Wanna play? (y/n): ").lower()
            except ValueError:
                print("invalid selection, choose y or n")
         
            if choice == "n":
                print("Thanks for coming bye") 
                break  
            try:
                die_count = int(input("choose number of dice(1,2): "))
           
                
                    
                if choice == "y" and die_count == 1:
                    die1 = random.randint(1, 6) 
                    print(die1)
                    
                elif choice == "y" and die_count == 2:   
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    print(f"{die1}, {die2}")
                else:
                    print("Decide if you wanna play or not") 
            except ValueError:
                     print("Select a valid input between 1 and 2")

                