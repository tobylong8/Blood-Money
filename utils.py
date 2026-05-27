from random import randint
from time import sleep

def roll_dice(sides, sides2=0, condition=None):
    if sides2 == 0:
        roll1 = randint(1,sides)
        roll2 = randint(1,sides)
        if condition == "advantage":
            roll = max(roll1, roll2)
        elif condition == "disadvantage":
            roll = min(roll1,roll2)
        else:
            roll = roll1
    else:
        roll1 = randint(1,sides)
        roll2 = randint(1,sides)
        roll3 = randint(1,sides2)
        roll4 = randint(1,sides2)
        if condition == "advantage":
            roll = max(roll1, roll2) + max(roll3, roll4)
        elif condition == "disadvantage":
            roll = min(roll1,roll2) + min (roll3, roll4)
        else:
            roll = roll1 + roll2
            print(f"{roll1} + {roll2}")
    return roll

def choice(number_of_choices):
    if number_of_choices == 2:
        while True:
            choice = input()
            if choice in ["1", "2"]:
                return choice
            print("Please enter 1 or 2.")
    elif number_of_choices == 3:
        while True:
            choice = input()
            if choice in ["1", "2", "3"]:
                return choice
            print("Please enter 1, 2, or 3.")
    elif number_of_choices == 4:
        while True:
            choice = input()
            if choice in ["1", "2", "3", "4"]:
                return choice
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
        print("Rolling...")
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
        print(f"You got a {total} ({roll} + {modifier}), meaning you succeed.")
        return result
    else:
        result = "failure"
        print(f"You got a {total} ({roll} + {modifier}), meaning you fail.")
        return result

def display_stats(player):
    print(f"\n--- {player.name} ---")
    print(f"Level: {player.level}")
    print(f"HP: {player.remaining_health}/{player.max_health}")
    print(f"AC: {player.ac}")
    print(f"Weapon: {player.weapon}")
    