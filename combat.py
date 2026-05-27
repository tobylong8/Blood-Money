from random import randint
from time import sleep
from characters import *
from utils import *

def player_initiative(player, condition=None):
    bonus = player.dexterity_modifier + player.proficiency_bonus
    if condition == "advantage":
        print("Rolling initiative with advantage...")
        roll = roll_dice(20, condition="advantage")
    elif condition == "disadvantage":
        print("Rolling initiative with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        print("Rolling initiative...")
        roll = roll_dice(20)
    total = roll + bonus
    sleep(2)
    print(f"You got {total} ({roll} + {bonus}).")
    return total

def player_attack(player, target_ac, condition=None):
    attack_modifier = player.attack_modifier
    damage_modifier = player.damage_modifier
    damage_dice = player.damage_dice
    if condition == "advantage":
        print("Rolling to-hit with advantage...")
        roll = roll_dice(20,condition="advantage")
    elif condition == "disadvantage":
        print("Rolling to-hit with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        print("Rolling to-hit...")
        roll = roll_dice(20)
    total = roll + attack_modifier
    sleep(2)
    if roll == 1:
        attack_result = "miss"
        print("You rolled a Natural 1, meaning you miss.\n")
    elif roll == 20:
        attack_result = "critical hit"
        print("You rolled a Natural 20, meaning you do double dice!")
    elif total >= target_ac:
        attack_result = "hit"
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you hit.")
    else:
        attack_result = "miss"
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you miss.\n")
        return "miss"
    sleep(1)
    if attack_result == "hit":
        damage_roll = roll_dice(damage_dice)
        damage = damage_roll + damage_modifier
        print("\n")
        print("Rolling damage...")
        sleep(2)
        print(f"You deal {damage} damage ({damage_roll} + {damage_modifier}).")
        print("\n")
        return damage
    elif attack_result == "critical hit":
        damage_roll = roll_dice(damage_dice) 
        damage_roll2 = roll_dice(damage_dice)
        damage = damage_roll + damage_roll2 + damage_modifier
        print("\n")
        print("Rolling damage...")
        sleep(2)
        print(f"You deal {damage} damage ({damage_roll} + {damage_roll2} + {damage_modifier}).")
        print("\n")
        return damage
