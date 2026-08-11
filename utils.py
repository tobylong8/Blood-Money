from random import randint
from time import sleep

def roll_dice(sides, condition=None):
    roll1 = randint(1,sides)
    roll2 = randint(1,sides)

    if condition == "advantage":
        roll = max(roll1, roll2)
    elif condition == "disadvantage":
        roll = min(roll1,roll2)
    else:
        roll = roll1

    return roll

def choice(number_of_choices):
    if number_of_choices == 2:
        while True:
            choice = input()
            if choice in ["1", "2"]:
                return choice
            print()
            print("Please enter 1 or 2.")
    elif number_of_choices == 3:
        while True:
            choice = input()
            if choice in ["1", "2", "3"]:
                return choice
            print()
            print("Please enter 1, 2, or 3.")
    elif number_of_choices == 4:
        while True:
            choice = input()
            if choice in ["1", "2", "3", "4"]:
                return choice
            print()
            print("Please enter 1, 2, 3 or 4.")

def pause():
    input("[Press Enter to Continue]")

def ability_check(player, skill, dc, condition=None):
    print(f"\n[Press enter to roll {skill}]")
    input()
    modifier = player.skills[skill]

    if condition == "advantage":
        print("Rolling with advantage...")
        roll = roll_dice(20, condition="advantage")
    elif condition == "disadvantage":
        print("Rolling with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        print("Rolling the d20...")
        roll = roll_dice(20)

    total = roll + modifier
    sleep(2)
    
    if roll == 1:
        result = "critical failure"
        print("You rolled a Natural 1, meaning you fail.")
        return result
    elif roll == 20:
        result = "critical success"
        print("You rolled a Natural 20, meaning you succeed!")
        return result
    elif total >= dc:
        result = "success"
        print(f"You got a total of {total} (your roll {roll} + your modifier {modifier}), meaning you succeed.")
        return result
    else:
        result = "failure"
        print(f"You got a total of {total} (your roll {roll} + your modifier {modifier}), meaning you fail.")
        return result

def display_stats(player):
    print(f"\n--- {player.name} ---")
    print(f"Level: {player.level}")
    print(f"HP: {player.remaining_health}/{player.max_health}")
    print(f"AC: {player.ac}")
    print(f"Weapon: {player.weapon}")