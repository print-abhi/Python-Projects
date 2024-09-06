import random

choices = ("Rock","Paper","Scissor")
player = None
computer = random.choice(choices)


player = input(("Enter Your Choice (Rock,Paper,Scissor):"))

print(f"Player: {player}")
print(f"Computer: {computer}")

while player not in choices:
    player = input("Enter Your Choice (Rock, Paper, Scissor): ").capitalize()
    if player not in choices:
        print("Invalid choice, please try again.")
        
if player ==computer:
    print("it's tie")
elif player == "Rock" and computer == "Scissor":
    print("You Win!")
elif player == "Paper" and computer == "Rock":
    print("You Win!")
elif player == "Scissor" and computer == "Paper":
    print("You Win!")
else:
    print("You lose !")


