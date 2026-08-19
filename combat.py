import random, sys
from time import sleep
from characters.player import Player
from characters.enemies import *
from utils import *

used_lines_tracker = {}

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

def player_attack(combat, player, enemy, condition=None):
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
        print()
        print(get_combat_text(combat, "player", "miss"))
        return "miss"
    elif roll == 20:
        attack_result = "critical hit"
        print("You rolled a Natural 20, meaning you do double dice!")
        print()
        print(get_combat_text(combat, "player", "critical_hit"))
    elif total >= enemy.ac:
        attack_result = "hit"
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you hit!")
        print()
        print(get_combat_text(combat, "player", "hit"))
    else:
        print(f"You got a {total} ({roll} + {attack_modifier}), meaning you miss")
        print()
        print(get_combat_text(combat, "player", "miss"))
        return "miss"
    
    pause()

    if attack_result == "hit":
        damage_roll = roll_dice(damage_dice)
        damage = damage_roll + damage_modifier
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

def enemy_attack(combat, enemy, player, condition=None):
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
        print()
        print(get_combat_text(combat, enemy.name.lower(), "miss"))
        return "miss"
    elif roll == 20:
        attack_result = "critical hit"
        print(f"{enemy.name} rolled a Natural 20, meaning he rolls double dice!")
        print()
        print(get_combat_text(combat, enemy.name.lower(), "critical_hit"))
    elif total >= player.ac:
        attack_result = "hit"
        print(f"{enemy.name} got a {total} ({roll} + {attack_modifier}), meaning he hits")
        print()
        print(get_combat_text(combat, enemy.name.lower(), "hit"))
    else:
        print(f"{enemy.name} got a {total} ({roll} + {attack_modifier}), meaning he misses")
        print()
        print(get_combat_text(combat, enemy.name.lower(), "miss"))
        return "miss"
    
    pause()

    if attack_result == "hit":
        damage_roll = roll_dice(damage_dice)
        damage = damage_roll + damage_modifier
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
    global used_lines_tracker
    
    combat_text = {
        "brawl": {
            "player": {
                "hit": [
                    "Your strike him hard in the cheekbone, sending a spray of sweat into the air",
                    "Your punch hits him directly in the nose, and you see his eyes water",
                    "You kick his shin, making him curse in pain",
                    "You clap his ears, making him hold his hands over them",
                    "You land a heavy blow to his stomach, hearing the air rush out of him as he staggers backwards",
                ],
                "critical_hit": [
                    "You hear a small crack as your knuckles hit his jaw. You have critically hit him!",
                    "You punch him hard in the ribs, and he jolts. You have critically hit him!",
                    "You punch his throat, and he gasps for air. You have critically hit him!",
                    "With all the energy you have, you swing your arm and uppercut him in the chin, sending him slightly in the air"
                ],
                "miss": [
                    "You swing a punch but Cole steps back, dodging the punch",
                    "You swing a punch for his nose but he ducks, dodging the punch",
                    "You punch his stomach, but it doesn't affect him at all",
                    "Your fist speeds past his ear as he jerks his head out of the way",
                    "You lunge forward with a punch, but he swats your arm aside and shoves you back",
                ],
                "dodge": [
                    "You raise your arms into a tight guard, making it harder for Cole's punches to connect",
                    "You drop your weight and widen your stance, ready for any attack that comes",
                    "You focus entirely on seeing any punches before they happen, ready to dodge",
                ],
                "death": [
                    "Cole's punch connects perfectly, and you fall on the hard floor, unconscious",
                ],
                "heal": [
                    "Gritting your teeth, you take a deep breath and steady your nerves, shaking off the pain"
                ]
            },

            "cole": {
                "hit": [
                    "Cole punches you hard in the chest, and you're slightly winded",
                    "Cole kicks you hard in the knee, and you're jolted slightly",
                    "Cole claps your ears, leaving them ringing horribly",
                    "Cole sends your knees straight into your gut, and you feel the air inside you escape",
                    "Cole delivers a mean right jab to your eye, and you feel your vision blur slighly"
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
                    "Cole tries to grab your neck but you just manage to escape his grip",
                ],
                "dodge": [
                    "Cole raises is arms in a defensive stance, making it harder to hit him",
                    "Cole tenses him abdomen and puts his arms around his head, making him like a brick wall",
                    "Cole takes a second to read you, trying to gauge when and how you'll punch, making it harder to hit him",
                ],
                "death": [
                    "Cole slumps against a nearby fence post, before sliding down into the dirt"
                ]
            }
        }
    }
    
    key = f"{combat}_{combatant}_{outcome}"
    all_lines = combat_text[combat][combatant][outcome]
    
    if key not in used_lines_tracker:
        used_lines_tracker[key] = []
        
    if len(used_lines_tracker[key]) == len(all_lines):
        used_lines_tracker[key].clear()

    available_lines = [line for line in all_lines if line not in used_lines_tracker[key]] 
    chosen_line = random.choice(available_lines)
    used_lines_tracker[key].append(chosen_line)
    
    return chosen_line

def combat(combat, *combatants, deadly=True):
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
                            player_attack(combat, player, target, "disadvantage")
                        else:
                            player_attack(combat, player, target)

                        if check_if_dead(target):
                            print()
                            print(get_combat_text(combat, target.name.lower(), "death"))

                        print()

                        if use_double_tap == "1" and i < num_attacks - 1:
                            pause()
                            clear()
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
                            print()

                elif chosen_action == "2":
                    print(get_combat_text(combat, "player", "dodge"))
                    player.dodging = True

                elif chosen_action == "3":
                    bonus = roll_dice(10) + player.level
                    player.remaining_health += bonus
       
                    if player.remaining_health > player.max_health:
                        player.remaining_health = player.max_health

                    player.grit_used = True
                    print(get_combat_text(combat, "player", "heal"))
                    print(f"You have {player.remaining_health}/{player.max_health} health")

                enemies_alive = any(not check_if_dead(c) for c in initiative_order if c is not player)
                if enemies_alive:
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
                            enemy_attack(combat, person, player, "disadvantage")
                        else:
                            enemy_attack(combat, person, player)
                        
                        if check_if_dead(player) == True:
                            if deadly == True:
                                print(get_combat_text(combat, "player", "death"))
                                pause()
                                clear()
                                display_stats(player)
                                sys.exit()
                            else:
                                print()
                                print(get_combat_text(combat, "player", "death"))
                                print()
                                break
                        
                elif enemy_action == "dodge":
                    print(get_combat_text(combat, person.name.lower(), "dodge"))
                    person.dodging = True
                    print()

                pause()

            clear()

        surviving_combatants = []
        for combatant in initiative_order:
            if not check_if_dead(combatant):
                surviving_combatants.append(combatant)
        initiative_order = surviving_combatants

        if len(initiative_order) <= 1 or player.remaining_health <= 0:
            break