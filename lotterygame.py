import secrets,sys
randomNumberGenerator = secrets.SystemRandom()
print ("_____Welcome to Our Game ________")

while True:
    print ("1. Age must be more than 18.\n2. Show money more than 5000. \n3. You must use more than 1000 each time.")
    permissionInput = input("Press 'y' for agree and 'n' for disagree:\n")
    if permissionInput == "n":
        print("See you again!!!")
        break
    elif permissionInput == "y":
        username = input("Please enter you username\n")
        age = int(input("Please enter you age\n"))
        if len(username) >2 and age>17:
            while True:
                print("You can play game now")
                print("Welcomw: ", username)
                while True:
                    smoney = int(input("Please enter your money\n"))
                    while smoney >4999:
                        print("This is your show money $", smoney)
                        while True:
                            if smoney < 1000:
                                print("Warning: You have not enough money")
                                break
                            playmoney = int(input("Please enter money to play\n"))
                            if playmoney>999:
                                while True:
                                    lucknumber = int(input("Please enter your lucky number two digit\n"))
                                    if len(str(lucknumber)) == 2:
                                        systemnumber = randomNumberGenerator.randint(10,99)
                                        if lucknumber == systemnumber:
                                            smoney += playmoney*10
                                            print("You won\n Your money $", smoney)
                                            continuegame = int(input("Press 0 to play game\n"))
                                            if continuegame == 0:
                                                break
                                            else:
                                                sys.exit()
                                        else:
                                            smoney -= playmoney
                                            print(f"Try again....Lucky Number is {systemnumber}\n Your money ${smoney}")
                                            continuegame = int(input("Press 0 to play game\n"))
                                            if continuegame == 0:
                                                break
                                            else:
                                                print("Bye Bye")
                                                sys.exit()
                                                
                                    else:
                                        print("Warning: Please enter lucky number within 2 digit")
                            else:
                                print("Warning: Play to money above 1000")
                                    
                    print("Warning: Please more money")
        else:
            print("Warning: Please read again rule")
    else:
        print("Warning: Please enter 'y' or  'n'")
        
