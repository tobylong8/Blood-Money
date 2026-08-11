from random import randint
from time import sleep
from characters.player import *
from characters.npcs import *
from characters.enemies import *
from utils import *

def roll_initiative(person, condition=None):
    bonus = person.initiative_modifier

    if condition == "advantage":
        if person == player:
            print("Rolling initiative with advantage...")
        else:
            print(f"{person.name} is rolling initiative with advantage...")
        roll = roll_dice(20, condition="advantage")
    elif condition == "disadvantage":
        if person == player:
            print("Rolling initiative with disadvantage...")
        else:
            print(f"{person.name} is rolling initiative with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        if person == player:
            print("Rolling initiative...")
        else:
            print(f"{person.name} is rolling initiative...")
        roll = roll_dice(20)

    total = roll + bonus
    #sleep(2) REMOVE HASHTAG LATER
    if person == player:
        print(f"You got {total} ({roll} + {bonus}).")
    else:
        print(f"{person.name} got {total} ({roll} + {bonus}).")

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

def combat(*combatants):
    initiative_order = [] 
    
    for person in combatants:
        roll = roll_initiative(person)
        initiative_order.append((roll, person))
        #sleep(1) REMOVE HASHTAG LATER
        print()

    initiative_order.sort(reverse=True)
    initiative_order = [person for total, person in initiative_order]

    print("--- Initiative Order ---")
    for person in initiative_order:
        print(person.name)

    ########################################
    print()

    while player.remaining_health > 0 and len(initiative_order) != 1:
        for person in initiative_order:
            if person == enemy_brother:
                continue
            if person == player:
                print("It is your turn. Would you like to:")
                print("1) Attack")
                print("2) Defend")
                action = choice(2)

                if action == "1":
                    choices = initiative_order.copy()
                    choices.remove(player)

                    print()
                    if len(choices) != 1:
                        print("Who would you like to attack:")
                        for index, enemy in enumerate(choices, start=1):
                            print(f"{index}) {enemy.name}")
                    else:
                        print(f"You attack {choices[0].name}")

            break
        break



            

        


