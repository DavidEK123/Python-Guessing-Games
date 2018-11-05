import random
def guessing_game():
    n = int(input("Enter a number from 0 to 100: "))
    num = random.randrange(0,100)

    while n != num:
        if n < num:
            print("Sorry," ,n, "is too low")
            n = int(input("Enter a number from 0 to 100: "))

        if n > num:
            print("Sorry," ,n, "is too high")
            n = int(input("Enter a number from 0 to 100: "))
        
    if n== num:
        print("you got it!")


guessing_game()    
