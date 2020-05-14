print ("      ")
\

y=int(input("\nChoose a lower limit for the range that the computer guesses within\n"))
x=int(input("\nChoose an upper limit for the range that the computer guesses within\n"))
attempts=0

guess=(x+y)/2

while True:
    if x < y:
        print ("Lower limit cannot be be greater than upper limit")
        print ("Restart the game with appropriate limits")
        break
    elif x > y:
        print ("Think of a number and tell me if my guess is right or not\n")
        print ("Is your number {}?".format(str(guess)))
        user_response = input("Yes/No:\n")
        if user_response == "Yes" or "yes":
            print ("I got it!, it took me {} attempts.".format(attempts))
            break
        elif user_response == "No" or "no":
            print("Was I too high or too low?")
            range_response = input("Too high/too low:\n")
            if range_response == "Too high":
                x=guess
                attempts +=1
            elif range_response == "Too low":
                 y=guess
                 attempts +=1
                 
