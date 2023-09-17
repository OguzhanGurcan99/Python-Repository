# Question 1
Theater = {"Satranç":[13,10],"Martı":[13,20],"Yeraltından Notlar":[13,5],"Küheylan":[7,25],"Köşebaşı":[18,7],"Paydos":[13,23],"Hamlet":[13,3],"Othello":[13,30],"Balkon":[18,8],"Yabancı":[18,15]}
#print(Theater)
plays = [x.strip().title() for x in Theater]
choice = input("Which theatre play would you like to watch ?:")
while True:
    if choice.lower().title() in plays:

        if choice in plays:
            age = int(input("Please enter your age: "))
            if age >= Theater[choice][0]:
                if Theater[choice][1]>0:
                    print("You bought one ticket. Enjoy the play!")
                    print(f"Tickets remain:{Theater[choice][1]-1}")
                else:
                    print("Sorry, we are sold out!")

            else:
                print("You are too young to see that play")

            break

        else:
            print("Please use correct naming convention for plays! Attention on letter cases.")
            choice = input("Which theatre play would you like to watch ?:")

    else:
        print("Sorry. We don't have that theater play...")
        choice = input("Which theatre play would you like to watch ?:")


# Question 2
import random
run_values = [random.randint(8,20) for i in range(10)]
print(run_values)

def track_run(x):
    progress_days= 0
    a = 0
    while a<len(x)-1:
        if x[a+1]>x[a]:
            progress_days +=1
        a+=1
    print(progress_days)
track_run(run_values)

# Question 3
number = int(input("Please enter a number:"))
divisor=[]
for i in range(1,number+1):
    if number % i ==0:
        divisor.append(i)
print(divisor)

# Question 4
user1 = input("What's your name?")
user2 = input("And your name?")

user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1,u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1=="rock":
        if u2=="paper":
            return "Paper wins!"
        else:
            return "Rock wins!"

    elif u1=="paper":
        if u2=="rock":
            return "Paper wins!"
        else:
            return "Scissors wins!"

    elif u1 =="scissors":
        if u2=="rock":
            return "Rock wins!"
        else:
            return "Scissors wins!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."

print(compare(user1_answer,user2_answer))
