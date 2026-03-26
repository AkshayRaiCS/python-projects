import random
from numberguessutils import save_game,gethigh_score, checkchangescore
class Guess:

    def __init__(self):
        self.attempts = 0
        open("savescore.txt","a").close()
        self.secret = random.randint(1,100)
        
    
    def play(self):
        while True:
            try:
                number = int(input("guess the number between 1-100"))
                self.attempts +=1
            except (ValueError):
                print("Enter the proper number between 1-100")
                continue
            if self.secret<number:
                print("Your number is Greater than the value")
                print("Try again")
            elif self.secret>number:
                print("Your number is Lesser than the value")
                print("Try again")
            if number==self.secret:
                print(f"You've got it right in {self.attempts} attempts")
                checkchangescore(self.attempts)
                break        

game = Guess()
game.play()
