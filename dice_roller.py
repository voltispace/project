import random

print("=" *22)
print(f"\033[105mWELCOME TO DICE ROLLER\033[0m")
print("=" *22)
    
    

def roll_dice():    
    choice = input("Wanna play? (y/n): ").lower()
          
    if choice == "n":
        print("Thanks for coming bye") 
            
    die_count = int(input("choose number of dice(1,2): "))
                             
    if choice == "y" and die_count == 1:
        die1 = random.randint(1, 6) 
        print(f"You rolled: {die1}")
                    
    elif choice == "y" and die_count == 2:   
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"You rollled: {die1}, {die2}. Your total is {total}")
    else:
        print("Decide if you wanna play or not") 
rounds = 1

while rounds <= 5:
        input(f"\n--- Round {rounds} --- Press Enter to roll...")
        roll_dice()
        rounds += 1  # Increment round count

print("\nGame over! You've used all 5 rolls.")