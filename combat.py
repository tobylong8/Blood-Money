import random
from time import sleep
from characters.player import Player
from characters.enemies import *
from utils import *

def check_if_dead(person):
    if person.remaining_health <= 0:
        return True
    else:
        return False

def roll_initiative(person, player, condition=None):
    bonus = person.initiative_modifier

    if condition == "advantage":
        if person is player:
            print("Rolling initiative with advantage...")
        else:
            print(f"{person.name} is rolling initiative with advantage...")
        roll = roll_dice(20, condition="advantage")
    elif condition == "disadvantage":
        if person is player:
            print("Rolling initiative with disadvantage...")
        else:
            print(f"{person.name} is rolling initiative with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        if person is player:
            print("Rolling initiative...")
        else:
            print(f"{person.name} is rolling initiative...")
        roll = roll_dice(20)

    total = roll + bonus
    sleep(1)
    if person is player:
        print(f"You got {total} ({roll} + {bonus})")
    else:
        print(f"{person.name} got {total} ({roll} + {bonus})")

    if roll == 20 and person is player:
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
        roll = roll_dice(20, condition="advantage")
    elif condition == "disadvantage":
        print(f"Rolling to-hit against {enemy.name} with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        print(f"Rolling to-hit against {enemy.name}...")
        roll = roll_dice(20)

    total = roll + attack_modifier
    sleep(1)

    if roll == 1:
        print("You rolled a Natural 1, meaning you miss")
        return "miss"
    elif roll == 20:
        attack_result = "critical hit"
        print("You rolled a Natural 20, meaning you do double dice!")
    elif total >= enemy.ac:
        attack_result = "hit"
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you hit!")
    else:
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you miss")
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
    else:
        raise ValueError(f"Unknown AI type: {enemy.ai_type}")

def enemy_attack(enemy, player, condition=None):
    attack_modifier = enemy.attack_modifier
    damage_modifier = enemy.damage_modifier
    damage_dice = enemy.damage_dice

    if condition == "advantage":
        print(f"{enemy.name} is rolling to hit against you with advantage...")
        roll = roll_dice(20, condition="advantage")
    elif condition == "disadvantage":
        print(f"{enemy.name} is rolling to hit against you with disadvantage...")
        roll = roll_dice(20, condition="disadvantage")
    else:
        print(f"{enemy.name} is rolling to hit against you...")
        roll = roll_dice(20)

    total = roll + attack_modifier
    sleep(1)

    if roll == 1:
        print(f"{enemy.name} rolled a Natural 1, meaning he misses")
        return "miss"
    elif roll == 20:
        attack_result = "critical hit"
        print(f"{enemy.name} rolled a Natural 20, meaning he rolls double dice!")
    elif total >= player.ac:
        attack_result = "hit"
        print(f"{enemy.name} got a {total} ({roll} + {attack_modifier}), meaning he hits")
    else:
        print(f"{enemy.name} got a {total} ({roll} + {attack_modifier}), meaning he misses")
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

def get_combat_text(combat, combatant, outcome):
    combat_text = {
        "brawl": {
            "player": {
                "hit": [
                    "Your strike him hard in the cheekbone",
                    "Your punch hits him directly in the nose, and you see his eyes water slightly",  # <--- Added comma here
                    "You kick his shin, making him curse in pain",
                    "You clap his ears, making him wince in pain",
                ],
                "critical_hit": [
                    "You hear a small crack as your knuckles hit his jaw. You have critically hit him!",
                    "You punch him hard in the ribs, and he jolts. You have critically hit him!",
                    "You punch his throat, and he gasps for air. You have critically hit him!",
                ],
                "kill": [
                    "You hear a thud as Cole falls to the ground after your devastating final blow",
                    "Cole topples to the ground after your devastating final blow",
                ],
                "miss": [
                    "You swing a punch but Cole steps back",
                    "You swing a punch for his nose but he ducks",
                    "You punch his stomach, but it doesn't affect him at all",
                ],
                "dodge": [
                    "You raise your arms into a tight guard, making it harder for Cole's punches to connect",
                    "You drop your weight and widen your stance, ready for any attack that comes",
                    "You focus entirely on seeing any punches before they happen, ready to dodge",
                ],
                "death": [
                    "Cole's punch connects perfectly, and you fall on the hard floor, unconscious",
                ]
            },

            "cole": {
                "hit": [
                    "Cole punches you hard in the chest, and you are slightly winded",
                    "Cole kicks you hard in the knee, but you manage to stay standing",
                    "Cole claps your ears, leaving them ringing horribly",
                ],
                "critical_hit": [
                    "Cole delivers a devastating punch to your left temple, and you feel your brain rattle inside your head. He critically hits",
                    "Cole punches you hard in the nose, and you feel excruciating pain. He critically hits",
                    "You lower your guard, and Cole punches you hard in the jaw, making your head jolt. He critically hits",
                ],
                "miss": [
                    "Cole swings at your face but you manage to step back, dodging the punch",
                    "Cole punches you in the gut but you absorb the blow",
                    "Cole tries to punch your face but you duck, dodging the blow",
                    "Cole sloppily throws a punch at you but he misses",
                ],
                "dodge": [
                    "Cole raises is arms in a defensive stance, making it harder to hit him",
                    "Cole tenses him abdomen and puts his arms around his head, making him like a brick wall",
                    "Cole takes a second to read you, trying to gauge when and how you'll punch",
                ]
            }
        },
    }

    return random.choice(combat_text[combat][combatant][outcome])


def combat(*combatants):
    player = next(person for person in combatants if isinstance(person, Player))
    initiative_order = []
    
    for person in combatants:
        roll = roll_initiative(person, player)
        initiative_order.append((roll, person))
        sleep(1)
        print()

    initiative_order.sort(
        key=lambda x: (x[0], x[1] is player),
        reverse=True
    )
    
    initiative_order = [person for total, person in initiative_order]

    print("--- Initiative Order ---")
    for combatant in initiative_order:
        print(combatant.name)

    pause()
    clear()

    while player.remaining_health > 0 and len([c for c in initiative_order if not check_if_dead(c)]) > 1:
        for person in list(initiative_order):
            if check_if_dead(person):
                continue

            person.dodging = False

            if person is player:
                print("--- Initiative Order ---")
                for combatant in initiative_order:
                    if not check_if_dead(combatant):
                        print(combatant.name)

                print()
                print("--- Player Stats ---")
                print(f"Health: {player.remaining_health}/{player.max_health} health")
                print(f"Double Tap used: {'Yes' if player.double_tap_used else 'No'}")
                print(f"Grit used: {'Yes' if player.grit_used else 'No'}")
                print()

                print("--- Enemy Stats ---")
                enemies = [combatant for combatant in initiative_order if combatant is not player and not check_if_dead(combatant)]
                for combatant in enemies:
                    print(f"{combatant.name}: {combatant.remaining_health}/{combatant.max_health} health")

                print("\nIt is your turn. Would you like to:")
                print("1) Attack")
                print("2) Dodge")

                if player.grit_used == False:
                    print("3) Heal (once per long rest)")
                    chosen_action = choice(3)
                else:
                    chosen_action = choice(2)
                    
                print()

                if chosen_action == "1":
                    use_double_tap = "2"
                    if not player.double_tap_used:
                        print("Would you like to use your once per long rest ability to do double attacks for one turn:")
                        print("1) Yes")
                        print("2) No")
                        if choice(2) == "1":
                            use_double_tap = "1"
                            player.double_tap_used = True
                        print()

                    num_attacks = (player.attacks_per_turn * 2) if use_double_tap == "1" else player.attacks_per_turn

                    for i in range(num_attacks):
                        choices = [
                            combatant for combatant in initiative_order 
                            if combatant != player and not check_if_dead(combatant)
                        ]
                        
                        if not choices:
                            break

                        if len(choices) > 1:
                            print(f"Who would you like to attack{(' with Double Tap' if use_double_tap == '1' else '')}:")
                            for index, enemy in enumerate(choices, start=1):
                                print(f"{index}) {enemy.name}")
                            target_idx = int(choice(len(choices))) - 1
                            target = choices[target_idx]
                        else:
                            target = choices[0]

                        print()

                        if target.dodging:
                            player_attack(player, target, "disadvantage")
                        else:
                            player_attack(player, target)

                        if check_if_dead(target):
                            print(f"{target.name} is dead")

                        print()

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

                pause()

            else:
                print("--- Initiative Order ---")
                for combatant in initiative_order:
                    if not check_if_dead(combatant):
                        print(combatant.name)

                print()
                print("--- Player Stats ---")
                print(f"Health: {player.remaining_health}/{player.max_health} health")
                print(f"Double Tap used: {'Yes' if player.double_tap_used else 'No'}")
                print(f"Grit used: {'Yes' if player.grit_used else 'No'}")
                print()

                print("--- Enemy Stats ---")
                enemies = [combatant for combatant in initiative_order if combatant is not player and not check_if_dead(combatant)]
                for combatant in enemies:
                    print(f"{combatant.name}: {combatant.remaining_health}/{combatant.max_health} health")

                print("\n")
                enemy_action = enemy_ai_decision(person)

                if enemy_action == "attack":
                    for i in range(person.attacks_per_turn):
                        if player.dodging == True:
                            enemy_attack(person, player, "disadvantage")
                        else:
                            enemy_attack(person, player)
                        
                        if check_if_dead(player) == True:
                            print("You are dead")
                            pause()
                            break
                        
                elif enemy_action == "dodge":
                    print(f"{person.name} takes a defensive stance and dodges!")
                    person.dodging = True

                pause()

            clear()

        surviving_combatants = []
        for combatant in initiative_order:
            if not check_if_dead(combatant):
                surviving_combatants.append(combatant)
        initiative_order = surviving_combatants

        if len(initiative_order) <= 1 or player.remaining_health <= 0:
            break