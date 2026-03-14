import random
fruits = ['apple','mango','litchi','papaya','banana','grapes','pineapple','strawberry']
sports = ['basketball','cricket','hockey','badminton','golf','swimming','race',]
animal = ['cat','dog','cow','monkey','giraff','lion','leapord','puma','horse']
language = ['python','javascript','c','react','java']

print("Welcome lets start the game, you have to be choose correct word until you get succeed.")

while True:
    print("Category avilable(fruits, sports, animal, language)")
    choice = input("Choose a category from the list : ").lower()
    if choice == 'fruits':
        curli = fruits
    elif choice == 'sports':
        curli = sports
    elif choice == 'animal':
        curli = animal
    elif choice == 'language':
        curli == language
    else:
        print("Chossing default fruit list")
        curli = fruits

    rwo = random.choice(curli)
    print("Length of chosen word is:",len(rwo))
    inp = input("Enter the word for match: ").lower()
    cou = 0
    while inp != rwo:
        cou+=1
        print("word start with: ",rwo[0:1])

        inp = input("Enter correct word: ").lower()
    print("Its true total attemps:",cou+1)
    lai = input("Want to exist or resume the game(resume/exit)")
    if(lai == 'resume'):
        continue
    elif(lai == 'exit'):
        print("Goodbye.")
        break
    else:
        print("Plese enter correct input (resume / exit)")
        
    