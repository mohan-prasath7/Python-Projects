import random
def generate_random_number(lower,upper):
    rand = random.randint(lower,upper)
    return rand
low = int(input("Enter the Lower Bound :"))
upper =int(input("Enter the Upper Bound :"))
guess = generate_random_number(low,upper)
print("You've only 7 chances to guess the integer!")
chance = 1
while chance <= 7:
    num = int(input("Guess a Number :"))
    if num == guess:
        print(f'Congradulatin you did it in {chance} try')
        break
    elif num > guess:
        print("You guessed too high!")
    else:
        print("You gussed too small!")
    chance +=1