import random

def roll_dice():
    return random.randint(1, 6)

def play():
    print("🎲 Welcome to Dice Game!")
    player_score = 0
    computer_score = 0
    for round in range(5):
        input(f"Round {round + 1}: Press Enter to roll the dice...")
        player = roll_dice()
        computer = roll_dice()
        print(f"You rolled:
