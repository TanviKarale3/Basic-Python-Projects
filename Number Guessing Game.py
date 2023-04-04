import random
Cnumber=random.randrange(1,101)
userInput=int(input("Enter your number-----"))
if userInput>Cnumber:
    print("Computer number",Cnumber)
    print("Your Guess no is too high")
elif Cnumber>userInput:
    print("Computer number",Cnumber)
    print("Your Guess no is too small")
else:
    print("Computer number",Cnumber)
    print("Your Guess no is equal")
