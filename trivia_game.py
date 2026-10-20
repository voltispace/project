import random

print("PLAY THE TRIVIA GAME\n")


x=0
while True:
    def begin(): # would you like to begin? yes/no... leaves if no
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
        return randomq(questions)

questions = {


'What planet is the hottest in our solar system?':
'Venus',

'What is the center of an atom called?':'Nucleus',

'What is the main gas that humans exhale?':
'Carbon dioxide',

'What organ do humans use to breathe?':
'Lungs',

'How many planets are in our solar system?':
8,

'What do you call an animal that eats only plants?':
'Herbivore',

'What part of the human body contains the most bones?':
'Hands',

'What is the largest land animal?':
'African elephant',

'What star is closest to Earth?':
'The Sun',

'What is the only metal that is liquid at room temperature?':
'Mercury'

}

for i, value in questions.items():
    print(value)
    options =random.choice(value)

# def 