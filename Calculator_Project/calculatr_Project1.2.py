from datetime import datetime
while True:
    userin = input("Enter the number , operator, number:")
    part = userin.split()

    if(part[1] == '+'):
        ans = int(part[0])+ int(part[2])
        print(ans)
        
    elif(part[1] == '-'):
        ans = int(part[0]) - int(part[2])
        print(ans)
        
    elif(part[1] == '*'):
        ans = int(part[0]) * int(part[2])
        print(ans)
    
    elif(part[1] == '/'):
        ans = int(part[0]) / int(part[2])
        print(ans)
        
    elif(part[1] == '%'):
        ans = int(part[0]) % int(part[2])
        print(ans)
        
    else:
        print("Mistake please enter correct input")

    times = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    suan = "Text -> "+ userin + " = " + str(ans) + ", saved at time - "+ times


    with open("history.txt",'a') as re:
        an = re.write( suan + '\n')
    finp = input("Want to see the history or next calculation or exit(yes/no/exit):").lower()
    if finp == 'yes':
        with open("history.txt",'r') as red:
            rea = red.read()
            print(rea)
    elif finp == 'no':
        continue
    elif finp == 'exit':
        print("Goodye! Hope you done your work.")
        break
    else:
        print("Invalid input, continuing to next calculation.")
