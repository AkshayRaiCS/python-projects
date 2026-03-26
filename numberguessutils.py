
def save_game(attempts):
    with open("savescore.txt","w") as file:
        file.write(f"{attempts}")
    
def gethigh_score():
    with open("savescore.txt","r") as file:
        x = int(file.read())
        return x
    
def checkchangescore(attempts):
    try:
        x = gethigh_score()
            
        if attempts <x:
            print("New high score")
            save_game(attempts)
            
        elif attempts >x:
            print(f"The best attempt remains {x}")
            
        else:
            print("Tied to the best attempt")
    except (ValueError,FileNotFoundError):
        print("New high score")
        save_game(attempts)
        


