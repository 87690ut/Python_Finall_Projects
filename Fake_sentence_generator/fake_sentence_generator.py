# 1. import random module
import random

#2. createing subject
subjects = ['Sachin tendulkar','Virat Kolhi', 'MS Dhoni','Salman khan','Shahrukh khan','Amir Khan','Amitabh bacchan','Jony sins','group of monkeys','group of elephants','group of lions']

#3.Creating actions
actions = ['launches missile','cancels dancing program','dances with anaconda','eats vimal paan masala','sleeps on flour','declares war','orders food','celebrate birthday','drives bullcart','dancing with buffalow','takes donkey ride']

#4. creating places
places =['in jaipur','in Mumbai','at gateway of india','in Amity univesity','at juhu beach','at himalya mountain','at red fort',]


# Starts sentence generating process

while True:

    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    sentence = f"{subject} {action} {place}"
    print("Breaking news:",sentence)
    userinp = input("Do you want more?(yes/no)").strip().lower()
    if userinp == 'no':
        break

print("Thanks for using our service.")
 
   














# sentence = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(places)}"
# print("Breaking news:",sentence)