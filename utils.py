from random import randint
from time import sleep
import os, subprocess

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

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

def choice(*number_of_choices):
    while True:
        choice = input()
        right_choices = [str(i) for i in range(1, number_of_choices[0] + 1)]
        if choice in right_choices:
            return choice
        print()
        print(f"Please enter a number between 1 and {number_of_choices[0]}.")  

def pause():
    print()
    input("[Press Enter to Continue]")
    print()

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