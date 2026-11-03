import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"You rolled: {die1} and {die2} (Total: {total})")

# Counter variable starting at 1
rounds = 1

while rounds <= 5:
    input(f"\n--- Round {rounds} --- Press Enter to roll...")
    roll_dice()
    rounds += 1  # Increment round count

print("\nGame over! You've used all 5 rolls.")
print('''There is a lucky charm to doing this
      count 3 if you want a tow six
      count fourif you want a 5 and 5''')