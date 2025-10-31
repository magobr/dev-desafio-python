message_initial = "Welcome to Jokenpo (Rock, Paper, Scissors)!"
message_instructions = "enter your choice (rock, paper, scissors): "

print(message_initial)

payer_one = input("Player_one, " + message_instructions).lower()
player_two = input("Player_tow, " + message_instructions).lower()

if payer_one == player_two:
    print("It's a tie!")
elif (payer_one == "rock" and player_two == "scissors") or \
     (payer_one == "paper" and player_two == "rock") or \
     (payer_one == "scissors" and player_two == "paper"):
    print("Player_one wins!")
else:
    print("Player_two wins!")    

