import random

print("PLAY THE TRIVIA GAME\n")
score =[]
def begin():
     while True:
            begin = input("Would you like to begin? (yes/no): ").lower()
            if begin == ("yes"):
                print ("Ok let's go!\n")
                get_username()#gets the user name
            elif begin != ("no") and begin != ("yes"):
                print ("I don't understand, please enter yes or no:")
                return begin()
            elif begin == ("no"):
                print ("Goodbye!")
            break

def get_username(): #get's username, checks whether it's the right length, says hello 
    username = input("Please choose a username (1-10 caracters):")
    if len(username)>10 or len(username)<1:
        print("Username too long or too short, try again")
        return get_username()
    else:
        print ("Hello", username, ", let's get started\n\n") 
        return randomq()

questions = [
    {
        "question": "What planet is the hottest in our solar system?",
        "answer": "venus"
    },
    {
        "question": "What is the center of an atom called?",
        "answer": "Nucleus"
    },
    {
        "question": "What is the main gas that humans exhale?",
        "answer": "Carbon dioxide"
    },
    {
        "question": "What organ do humans use to breathe?",
        "answer": "Lungs"
    },
    {
        "question": "How many planets are in our solar system?",
        "answer": "8"
    },
    {
        "question": "What do you call an animal that eats only plants?",
        "answer": "Herbivore"
    },
    {
        "question": "What part of the human body contains the most bones?",
        "answer": "Hands"
    },
    {
        "question": "What is the largest land animal?",
        "answer": "African elephant"
    },
    {
        "question": "What star is closest to Earth?",
        "answer": "The Sun"
    },
    {
        "question": "What is the only metal that is liquid at room temperature?",
        "answer": "Mercury"
    }
]
def randomq():
    rounds=1
    while rounds <=5:
    
        try:
            choice = int(input("Pick your question number (1-10):\n"))
        except ValueError:
            print("choose a valid number")
            return randomq
        
        if choice < 0 or choice > len(questions):
            print("choice is out of range, choose btw 1-10")
            return randomq
    
        print(questions[choice-1]['question'])
        try:
            ans = input("Write you answer\n")
        except ValueError:
            print("Answer must be in words")
            continue
            
        answer = questions[choice-1]["answer"]
        
        if ans.strip().lower() == answer.lower():
            print("Correct! you earned 2 points ")
            score.append(2) 
        else:
            print("Your answer is incorrect, try again")
            score.append(0)
        rounds+=1
                          
    total= sum(score)
    print(f"You scored {score}")
    print(f"Your total score is: {total}")
    
    decision = input("You have exhausted your 5 rounds, do you want to play again? (yes/no):\n")
    if decision == "yes":
        randomq()
    else:
        exit
        
       
begin()
