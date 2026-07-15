import random

# Game setup variables
Highscore = 0
Recent_score = []

# Mapping dictionaries
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

print("=== Welcome to Snake, Water, Gun! ===")
print("Rules: s = Snake, w = Water, g = Gun\n")

while True:
    # 1. Ask the player for their move or if they want to quit
    user_input = input("Enter your choice (s/w/g) or 'q' to Quit: ").strip().lower()
    
    if user_input == "q":
        print("\nThanks for playing!")
        break
        
    if user_input not in youDict:
        print("Invalid input! Please enter 's', 'w', 'g', or 'q'.\n")
        continue

    # 2. Setup choices
    computer = random.choice([-1, 0, 1])
    you = youDict[user_input]
    
    print("-" * 30)
    print(f"You chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")
    print("-" * 30)

    # 3. Game Logic & Score Updating
    if computer == you:
        print("Its a draw!\n")
        # Optional: You can choose to append the unchanged highscore here
        
    else:
        # Win Conditions for Player
        if (
            (computer == -1 and you == 1) or  # Water vs Snake (Snake drinks Water -> Win)
            (computer == 1 and you == 0) or   # Snake vs Gun (Gun shoots Snake -> Win)
            (computer == 0 and you == -1)     # Gun vs Water (Gun sinks in Water -> Win)
        ):
            print(" You Win! (+500 points)\n")
            Highscore += 500
            
        # Lose Conditions for Player
        else:
            print("You Lose!\n")
            
    # Track the score progression
    Recent_score.append(Highscore)

# 4. Save the final Highscore to the file after exiting the loop
with open("Hi-score.txt", "a") as f:
    f.write(str(Highscore) + "\n")

print(f"Game Over!  Highscore :  {Highscore} ")
print(f"Score History: {Recent_score}")