import random
print("Winning rules of the game ROCK PAPER SCISSORS are: ")
print("Rock vs Paper -> Paper wins ")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins ")
print("Enter Your Choice")
print(" 1 - Rock ")
print(" 2 - Paper")
print(" 3 - Scissors ")
computer = ["Rock","Paper","Scissors"]

while 1:
    player=""
    n = int(input("Enter your Choice :"))
    if n == 1:
        player = "Rock"
    elif n == 2:
        player = "Paper"
    elif n==3:
        player = "Scissors"
    else:
        print("Error!! Enter the Valid Option")
    print(f"User Choice is {player}")
    print("Now it's Computer's Turn...")
    cp=random.choice(computer)
    print(f"Computer choice is: {cp}")
    print(f"{player} vs {cp}")
    if player =="Rock" and cp =="Paper":
        print("<== Computer wins! ==>")
    elif player == "Paper" and cp == "Rock":
        print("<== Congradulations You're win! ==>")
    elif player =="Scissors" and cp =="Rock":
        print("<== Computer wins! ==>")
    elif player == "Rock" and cp == "Scissors":
        print("<== Congradulations You're win! ==>")
    elif player =="Paper" and cp =="Scissors":
        print("<== Computer wins! ==>")
    elif player == "Scissors" and cp == "Paper":
        print("<== Congradulations You're win! ==>")
    else:
        print("<== It's a tie! ==>")
    p = input("Do you want to play again? (Y/N) :")
    if p == "N" or p =="n":
        break
print("Thanks for Playing !")

