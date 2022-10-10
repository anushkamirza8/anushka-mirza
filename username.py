username = 'Anushka'

password = 'Bob'

userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome!")
        import runningoutoftime5.py
    else:
        print("That is the wrong password.")
        exit()
else:
    print("That is the wrong username.")
