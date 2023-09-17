import random
number = random.randint(1,100)

guess = int(input("take a new guess:"))
guesses = [guess]

while True:
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        guess = int(input("take a new guess:"))
    else:
        if number == guess:
            print("Congratulations!")
            print("It took {} guesses to win".format(len(guesses)))
            break

        else:
            if len(guesses)== 1:
                distance = abs(number-guess)
                if distance <= 10:
                    print("WARM")
                else:
                    print("COLD")

                guess = int(input("take a new guess:"))
                guesses.append(guess)
            else:
                previousGuess = guesses[-2]
                distance1= abs(previousGuess-number)
                distance2= abs(guess-number)

                if distance1<distance2:
                    print("COLDER")
                else:
                    print("WARMER")

                guess = int(input("take a new guess:"))
                guesses.append(guess)

