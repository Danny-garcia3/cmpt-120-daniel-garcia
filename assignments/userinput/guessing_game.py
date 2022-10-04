
def start():

    answer = "turtle"
    guess_limit = 3
    guess_count = 0
    
    print("Try and guess the animal, you have three guesses before the game is over!")
    while guess_count < guess_limit:
        guess = input("Enter Animal: ").lower()
        guess_count += 1
        if guess == answer:
            print("you guessed it right!")
            break
        elif guess == "quit":
            print("Exiting...")
            break
        else:
            print("The animal is not right! try again!")
start()