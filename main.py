import random

possible_options = ["R", "P", "S"]
opt = {
    'R': "Rock",
    'S': "Scissors",
    'P': "Paper"}

while True:
    user_input = input("Pick an option between 'R', 'P', or 'S': ").upper()

    if user_input not in possible_options:
        print("Error. Pick another option.")
    
    CPU = random.choice(possible_options)    
        
    if user_input == CPU:
        print(f"Player ({opt.get(user_input)}) : CPU ({opt.get(CPU)})")  
        print("The game is tied. Play again.")
    elif user_input == "S":
        if CPU == "R":
            print(f"Player ({opt.get(user_input)}) : CPU ({opt.get(CPU)})")
            print("CPU wins, you lost. Rock beats Scissors.") 
            break
        if CPU == "P":
            print(f"Player ({opt.get(user_input)}) : CPU ({opt.get(CPU)})")
            print("You win! Scissors beats Paper.")
            break
    elif user_input == "R":
        if CPU == "P":
            print(f"Player ({opt.get(user_input)}) : CPU ({opt.get(CPU)})")
            print("CPU wins, you lost. Paper beats Rock.")
            break
        if CPU == "S":
            print(f"Player ({opt.get(user_input)}) : CPU ({opt.get(CPU)})")
            print("You win! Rock beats Scissors.")
            break
    elif user_input == "P":
        if CPU == "S":
            print(f"Player ({opt.get(user_input)}) : CPU ({opt.get(CPU)})")
            print("CPU wins, you lost. Scissors beats Paper.")
            break
        if CPU == "R":
            print(f"Player ({opt.get(user_input)}) : CPU ({opt.get(CPU)})")
            print("You win! Paper beats Rock.")
            break
    else:
        continue           

