import random

opt = {
    'R': "Rock",
    'S': "Scissors",
    'P': "Paper"}

while True:
    possible_options = ["R", "P", "S"]

    CPU = random.choice(possible_options)
    user_option = None
    user_option = input("Pick an option between 'R', 'P', or 'S': ").upper()


    if user_option == CPU:
        print(f"Player ({opt.get(user_option)}) : CPU ({opt.get(CPU)})")  
        print("The game is tied. Play again.")
    elif user_option == "S":
        if CPU == "R":
            print(f"Player ({opt.get(user_option)}) : CPU ({opt.get(CPU)})")
            print("You lost. Rock beats Scissors") 
            break
        if CPU == "P":
            print(f"Player ({opt.get(user_option)}) : CPU ({opt.get(CPU)})")
            print("You win! Rock beats Paper")
            break
    elif user_option == "R":
        if CPU == "P":
            print(f"Player ({opt.get(user_option)}) : CPU ({opt.get(CPU)})")
            print("You lost. Paper beats Rock")
            break
        if CPU == "S":
            print(f"Player ({opt.get(user_option)}) : CPU ({opt.get(CPU)})")
            print("You win! Rock beats Scissors")
            break
    elif user_option == "P":
        if CPU == "S":
            print(f"Player ({opt.get(user_option)}) : CPU ({opt.get(CPU)})")
            print("You lost. Scissors beats Paper")
            break
        if CPU == "R":
            print(f"Player ({opt.get(user_option)}) : CPU ({opt.get(CPU)})")
            print("You win! Paper beats Rock")
            break
    if user_option not in possible_options:
        print("Error. Try Again")
    else:
        continue           

