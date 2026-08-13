import random
from random import randint
from time import sleep
from characters.player import *
from characters.npcs import *
from characters.enemies import *
from utils import *

def check_if_dead(person):
    if person.remaining_health <= 0:
        return True
    else:
        return False

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
    sleep(1)
    if person == player:
        print(f"You got {total} ({roll} + {bonus})")
    else:
        print(f"{person.name} got {total} ({roll} + {bonus})")

    if roll == 20 and person == player:
        total += 100
    elif roll == 20:
        total += 50

    return total

def player_attack(player, enemy, condition=None):
    attack_modifier = player.attack_modifier
    damage_modifier = player.damage_modifier
    damage_dice = player.damage_dice

    if condition == "advantage":
        print(f"Rolling to-hit against {enemy.name} with advantage...")
        roll = roll_dice(20,condition="advantage")
    elif condition == "disadvantage":
        print(f"Rolling to-hit against {enemy.name} with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        print(f"Rolling to-hit against {enemy.name}...")
        roll = roll_dice(20)

    total = roll + attack_modifier
    sleep(1)

    if roll == 1:
        attack_result = "miss"
        print("You rolled a Natural 1, meaning you miss\n")
        return "miss"
    elif roll == 20:
        attack_result = "critical hit"
        print("You rolled a Natural 20, meaning you do double dice!")
    elif total >= enemy.ac:
        attack_result = "hit"
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you hit!")
    else:
        attack_result = "miss"
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you miss\n")
        return "miss"
    
    sleep(1)

    if attack_result == "hit":
        damage_roll = roll_dice(damage_dice)
        damage = damage_roll + damage_modifier
        print()
        print("Rolling damage...")
        sleep(1)
        print(f"You deal {damage} damage ({damage_roll} + {damage_modifier})")
        print()
        enemy.remaining_health -= damage
        if check_if_dead(enemy) == True:
            enemy.remaining_health = 0
            return
        print(f"{enemy.name} has {enemy.remaining_health}/{enemy.max_health} health")
        return damage
    elif attack_result == "critical hit":
        damage_roll = roll_dice(damage_dice) 
        damage_roll2 = roll_dice(damage_dice)
        damage = damage_roll + damage_roll2 + damage_modifier
        print()
        print("Rolling damage...")
        sleep(1)
        print(f"You deal {damage} damage ({damage_roll} + {damage_roll2} + {damage_modifier})")
        print()
        enemy.remaining_health -= damage
        if check_if_dead(enemy) == True:
            enemy.remaining_health = 0
            return
        print(f"{enemy.name} has {enemy.remaining_health}/{enemy.max_health} health")
        return damage

def enemy_ai_decision(enemy):
    if enemy.ai_type == "balanced":
        if enemy.remaining_health < (enemy.max_health * 0.3):
            choices = ["attack", "dodge", "dodge", "dodge"] 
        else:
            choices = ["attack", "attack", "attack", "attack", "attack", "attack", "attack", "dodge", "dodge", "dodge"]
        
        chosen_action = random.choice(choices)
        return chosen_action
    
    elif enemy.ai_type == "brute":
        if enemy.remaining_health < (enemy.max_health * 0.3):
            choices = ["attack", "attack", "dodge", "dodge"] 
        else:
            choices = ["attack", "attack", "attack", "attack", "attack", "attack", "attack", "attack", "attack", "dodge"]
        
        chosen_action = random.choice(choices)
        return chosen_action

def enemy_attack(enemy, condition=None):
    attack_modifier = enemy.attack_modifier
    damage_modifier = enemy.damage_modifier
    damage_dice = enemy.damage_dice

    if condition == "advantage":
        print(f"{enemy.name} is rolling to hit against you with advantage...")
        roll = roll_dice(20,condition="advantage")
    elif condition == "disadvantage":
        print(f"{enemy.name} is rolling to hit against you with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        print(f"{enemy.name} is rolling to hit against you...")
        roll = roll_dice(20)

    total = roll + attack_modifier
    sleep(1)

    if roll == 1:
        attack_result = "miss"
        print(f"{enemy.name} rolled a Natural 1, meaning he misses\n")
        return "miss"
    elif roll == 20:
        attack_result = "critical hit"
        print(f"{enemy.name} rolled a Natural 20, meaning he rolls double dice!")
    elif total >= player.ac:
        attack_result = "hit"
        print(f"{enemy.name} got a {total} ({roll} + {attack_modifier}), meaning he hits")
    else:
        attack_result = "miss"
        print(f"{enemy.name} got a {total} ({roll} + {attack_modifier}), meaning he misses\n")
        return "miss"
    
    sleep(1)

    if attack_result == "hit":
        damage_roll = roll_dice(damage_dice)
        damage = damage_roll + damage_modifier
        print()
        print("Rolling damage...")
        sleep(1)
        print(f"{enemy.name} deals {damage} damage ({damage_roll} + {damage_modifier})")
        print()
        player.remaining_health -= damage
        if check_if_dead(player) == True:
            player.remaining_health = 0
            return
        print(f"You have {player.remaining_health}/{player.max_health} health")
        return damage
    elif attack_result == "critical hit":
        damage_roll = roll_dice(damage_dice) 
        damage_roll2 = roll_dice(damage_dice)
        damage = damage_roll + damage_roll2 + damage_modifier
        print()
        print("Rolling damage...")
        sleep(1)
        print(f"{enemy.name} deals {damage} damage ({damage_roll} + {damage_roll2} + {damage_modifier})")
        print()
        player.remaining_health -= damage
        if check_if_dead(player) == True:
            player.remaining_health = 0
            return
        print(f"You have {player.remaining_health}/{player.max_health} health")
        return damage

def combat(*combatants):
    initiative_order = []
    
    for person in combatants:
        roll = roll_initiative(person)
        initiative_order.append((roll, person))
        sleep(1)
        print()

    initiative_order.sort(
        key=lambda x: (x[0], x[1] == player), 
        reverse=True
    )
    
    initiative_order = [person for total, person in initiative_order]

    print("--- Initiative Order ---")
    for person in initiative_order:
        print(person.name)

    print()

    while player.remaining_health > 0 and len(initiative_order) != 1:
        for person in initiative_order:
            person.dodging = False

            if person == player:
                print("It is your turn. Would you like to:")
                print("1) Attack")
                print("2) Dodge")
                print("3) Heal (once per long rest)")
                chosen_action = choice(3)
                print()

                if chosen_action == "1":
                    if player.double_tap_used == True:
                        choices = [
                            person
                            for person in initiative_order
                            if person != player and not check_if_dead(person)
                        ]

                        if len(choices) != 1:
                            print("Who would you like to attack:")
                            for index, enemy in enumerate(choices, start=1):
                                print(f"{index}) {enemy.name}")
                            target = choice(len(choices))
                            target = choices[int(target) - 1]
                            if target.dodging == True:
                                player_attack(player, target, "disadvantage")
                            else:
                                player_attack(player, target)
                        else:
                            if choices[0].dodging == True:
                                player_attack(player, choices[0], "disadvantage")  
                            else:
                                player_attack(player, choices[0])
                    else:
                        print("Would you like to use your once per long rest ability to do double attacks for one turn:")
                        print("1) Yes")
                        print("2) No")
                        use_double_tap = choice(2)
                        print()
                        if use_double_tap == "2":
                            choices = [
                                person
                                for person in initiative_order
                                if person != player and not check_if_dead(person)
                            ]
    
    
                            if len(choices) != 1:
                                print("Who would you like to attack:")
                                for index, enemy in enumerate(choices, start=1):
                                    print(f"{index}) {enemy.name}")
                                target = choice(len(choices))
                                target = choices[int(target) - 1]
                                if target.dodging == True:
                                    player_attack(player, target, "disadvantage")
                                else:
                                    player_attack(player, target)
                            else:
                                if choices[0].dodging == True:
                                    player_attack(player, choices[0], "disadvantage")  
                                else:
                                    player_attack(player, choices[0])
                        else:
                            for i in range(player.attacks_per_turn * 2):
                                choices = [
                                    person
                                    for person in initiative_order
                                    if person != player and not check_if_dead(person)
                                ]
        
                                if len(choices) != 1:
                                    print("Who would you like to attack:")
                                    for index, enemy in enumerate(choices, start=1):
                                        print(f"{index}) {enemy.name}")
                                    target = choice(len(choices))
                                    target = choices[int(target) - 1]
                                    if target.dodging == True:
                                        player_attack(player, target, "disadvantage")
                                    else:
                                        player_attack(player, target)
                                else:
                                    if choices[0].dodging == True:
                                        player_attack(player, choices[0], "disadvantage")  
                                    else:
                                        player_attack(player, choices[0])
                            player.double_tap_used = True

                elif chosen_action == "2":
                    print("You dodge")
                    player.dodging = True

                elif chosen_action == "3":
                    bonus = roll_dice(10) + player.level
                    player.remaining_health += bonus
   
                    if player.remaining_health > player.max_health:
                        player.remaining_health = player.max_health

                    player.grit_used = True
                    print(f"You have {player.remaining_health}/{player.max_health} health")


                surviving_combatants = []
                for person in initiative_order:
                    if check_if_dead(person):
                        if person == player:
                            print("You are dead\n")
                        else:
                            print(f"{person.name} is dead\n")
                    else:
                        surviving_combatants.append(person)

                initiative_order = surviving_combatants

            else:
                enemy_action = enemy_ai_decision(person)

                if enemy_action == "attack":
                    for i in range (person.attacks_per_turn):
                        if player.dodging == True:
                            enemy_attack(person, "disadvantage")
                            print()
                        else:
                            enemy_attack(person)
                            print()
                        
                        if check_if_dead(player) == True:
                            break
                        
                elif enemy_action == "dodge":
                    print()
                    print(f"{person.name} takes a defensive stance and dodges!")
                    print()
                    person.dodging = True

                surviving_combatants = []
                for person in initiative_order:
                    if check_if_dead(person):
                        if person == player:
                            print("You are dead\n")
                        else:
                            print(f"{person.name} is dead\n")
                    else:
                        surviving_combatants.append(person)

                initiative_order = surviving_combatants