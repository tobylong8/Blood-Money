from random import randint
from time import sleep
from characters.player import *
from characters.enemies import *
from characters.npcs import *
from utils import *
from combat import *
import pyfiglet

def intro():
    clear()
    print("=" * 65 + "\n")
    print(pyfiglet.figlet_format("BLOOD     MONEY", font="smslant"))
    print("=" * 65) 
    print("\n")
    print("Blood Money is a text-based western adventure with Dungeons and Dragons mechanics.")
    print("You will make choices, roll dice, and live with the consequences.\n")
    print("To make a choice, type the corresponding number and press enter")
    print("Some choices will trigger ability checks — the outcome depends on your stats and the roll of a dice\n")
    print("You play as John Calloway, an infamous outlaw and hired gun with the best shot in the state")
    print("And the last man who should ever trust a stranger buying him a drink\n")
    print("As you progress through the story you will gain abilities\n")
    print("Currently you have 2 abilities that you can use once per long rest:")
    print("Double Tap - doubles the number of attacks for one turn")
    print("Grit - heals hit points equal to 1d10 + your level\n")
    print("Would you like to start the game (1), or get a quick overview of the mechanics (2)?")
    choice1 = choice(2)

    if choice1 == "2":
        print()
        print("Dice notation is a shortened way of describing what dice is being rolled. The 'd' stands for dice, and the number following it represents the number of sides on that dice.")
        print("A Natural 20 is rolling a 20 (the best result) and a Natural 1 is rolling a 1 (the worst result)")
        pause()
        print("Ability checks are used when a character tries to perform an action that has a chance of failure (other than attacking an enemy). The game rolls a 20-sided die and adds a specific modifier tied to that character's stats (like strength or intelligence). If the final total meets or beats a target number set by the game, the action succeeds. Special conditions like advantage (rolling two dice and taking the higher result) or disadvantage (rolling two and taking the lower) can modify these rolls.")
        pause()
        print("Combat is structured in a turn-based loop:")
        pause()
        print("Initiative: At the start of a fight, everyone rolls a d20 plus their initiative modifier to determine the turn order. (rolling a Natural 20 puts you first in initiative automatically).")
        pause()
        print("Turns & Actions: During a turn, characters can choose to attack, dodge (which gives incoming attackers disadvantage), or use items/abilities.")
        pause()
        print("To-Hit vs. AC: When attacking, a player or enemy rolls a d20 plus an attack modifier. If the total meets or beats the target's Armor Class (AC), the attack hits, and damage dice are rolled to reduce the target's remaining health.")
        print("Rolling a Natural 20 results in a critical hit for extra damage, and rolling a Natural 1 means you automatically miss\n")
        input("[Press Enter to Start the Game]")
    if choice1 == "1":
        pass

def duel():
    clear()
    global lost_duel, cheated_in_duel, lost_brawl
    lost_duel = False
    lost_brawl = False
    cheated_in_duel = False
    print("June 7th, 1872. You stand in hot summer sun, facing a large, angry man on the other side of the street. You lock eyes, gripping your holsters, and you feel a bead of sweat drip from your brow. There's a hushed crowd, and you see a mother cover her boy's eyes.")
    print("\n'I'm sending you straight to hell!' He shouts, his mean eyes staring intensely into yours.\n")
    print("Would you like to antagonise him (1), persuade him not to fight (2), or not respond (3)?")
    choice1 = choice(3)

    if choice1 == "1":
        print("\nYou respond, wiping the barrel of your revolver with a cloth. 'Last feller that talked to me like that ain't talkin' no more.'")
        intimidation_result = ability_check(player, "intimidation", 12)

        if intimidation_result == "success":
            print("\nYou sense the man's cocky tone fade. You see him gulp before he shakes it off.")
            print("'Enough now.' He says, 'Let's just get this over with.'\n")

        if intimidation_result == "critical success":
            print("\nThe man's expression fades, and he drops his gun. He tries to run away, but his legs are frozen. One of his friends picks up his revolver and hands it back to him, patting him on the back.")
            print("You have advantage in the duel.\n")
            print("He pleads with his friends to cancel the duel, but they reject him: 'Come on now, when you win I'll buy us all drinks.' He nods, shaking slightly, before facing you again.\n")

        if intimidation_result == "failure":
            print("\nYou see the man smirk, before chuckling to himself. 'You really aren't as tough as you thought, friend. Let's just get this done before you say something else stupid.'\n")

        if intimidation_result == "critical failure":
            print("\nAs you attempt to intimidate him, your voice goes hoarse. You see the man cackle to himself, and a few members of the crowd join in. 'This might me the funniest duel I have ever done.' The man says, before chuckling some more.")
            print("Your embarrassment causes you to have disadvantage in the duel.\n")
            print("'I feel kinda bad that I'm about to kill you now.' He says, still smiling.\n")    

    elif choice1 == "2":
        print("\nYou attempt to persuade him, 'Come on now, there's no need to fight. It was just a joke.'")
        persuasion_result = ability_check(player, "persuasion",15)

        if persuasion_result == "success" or persuasion_result == "critical success":
            print("\n'Guess we shouldn't fight with the kids around' He says, his angry expression fading.")
            print("Suddenly, you see his friend slap him. 'What the hell has gotten into you, you're just going to let him get away with insulting your mother!'")
            print("He remains silent for a few seconds, before his angry expression returns. 'You damn bastard.'\n")

        elif persuasion_result == "failure":
            print("\nYou see that his angry expression isn't gone.")
            print("'It's too late now to apologize now you damn coward!' He shouts, furiously looking at you.\n")

        elif persuasion_result == "critical failure":
            print("\nAfter your attempt to persuade him, he looks furious. He points his revolver to the sky and shoots. You see people stand back.")
            print("'IF YOU THINK YOU CAN BE A GODDAMN COWARD AFTER INSULTING MY MOTHER, THEN YOU CAN GO AND SHOOT YOURSELF!'\n")    

    elif choice1 == "3":
        print("\nYou remain silent, staring itently into his eyes. He stays quiet after that.")

    pause()
    clear()
    print("A few tense seconds of silence pass, where the only thing you hear is the howling wind. Eventually, the silence is broken when a man from the crowd mutters: 'When is this duel gonna start goddamnit?'\n")
    print("A tall man wearing a long, brown coat with a silver star pinned to his chest emerges from the crowd, 'Hello gentlemen, I'm Sheriff Briggs. I'll be overseeing this duel, and I want to see a fair game from both of you.'\n")
    print("'I will count to 10. When I say 10, you can start shooting. If you shoot earlier than 10, there will be consequences.'\n")
    print("The sheriff stands in the middle of the street, he clears his throat and begins counting: '1, 2, 3, 4.'\n")
    print("Would you like to comply with the rules and wait for 10 seconds (1), or shoot at him early (2)?")
    choice2 = choice(2)

    if choice2 == "1":
        print("\nThe sheriff continues counting. You see your opponent gripping his holster, anxiously waiting for when he says 10. You lock eyes, like a predator staring down its prey.")
        print("A few more seconds pass, until the sheriff shouts '8, 9, 10!'")
        print("You are primed with your revolver as you take it out of your holster. The man fumbles his. 'Goddamn holster, never works right!'\n")
        input("[Press enter to fire your revolver].")
        print("Firing...\n")
        sleep(2)
        roll = roll_dice(20)

        if roll < 5:
            print("You pull the trigger, but the shot goes wide, speeding past his ear. You try to shoot again but your revolver is jammed. The man unholsters his revolver and fires it.")
            dive = ability_check(player, "acrobatics", 8)

            if dive == "success" or dive == "critical success":
                print("\nYou dive to the side, dodging the bullet. While lying down, you point your revolver at the man's head.\n")
                input("[Press enter to fire your revolver].")
                print("Firing...\n")
                sleep(2)
                print("You pull the trigger, and the bullet speeds through the air, and within less than a second, it hits the man square in the forehead. He falls to the floor, a gaping wound spewing blood. The crowd of people go silent. You get up from the ground and put your revolver back in your holster\n")

            elif dive == "failure":
                print("You try and dive but it is too late. The bullet goes straight into your left shoulder.\n")
                player.remaining_health -= randint(3, 5)
                print("You lay on the ground for a few seconds, clutching your shoulder. Several bullets narrowly miss you. Through the constant ringing, you hear the man yell about running out of ammo. You hear sprinting footsteps coming towards you. You turn towards him, and you see him running full force with a knife in his hand. You point the revolver at him.\n")
                input("[Press enter to fire your revolver].")
                print("Firing...\n")
                sleep(2)
                print("Through the nauseating pain, you pull the trigger, and the bullet speeds through the air, and it hits the man in the chest. He falls to the floor, a gaping wound spewing blood. The crowd of people go silent. You put your revolver back in your holster, your left hand pressed tight against your bullet wound.")
                pause()
                print("You begin to feel dizzy, and you fall unconscious.")
                lost_duel = True

        else:
            print("You pull the trigger, and the bullet speeds through the air, and within less than a second, it hits the man square in the forehead. He falls to the floor, a gaping wound spewing blood. The crowd of people go silent, then you hear hushed whispers. You put your revolver back in your holster.\n")

        print("Suddenly, a tall, muscular man, storms up to you. 'That's my brother you just shot, you're a dead man!'")
        print("You see one of his friends yell: 'Cole is gonna wipe the floor with you!'")
        pause()
        clear()
        combat("brawl", player, cole, deadly=False)

        if player.remaining_health == 0:
            lost_brawl = True

    elif choice2 == "2":
        cheated_in_duel = True
        print("\nThe sheriff continues counting. You see your opponent gripping his holster, anxiously waiting for when he says 10. You lock eyes, like a predator staring down its prey.")
        print("A few more seconds pass, but before the sheriff says 10, you take out your revolver.\n")
        input("[Press enter to fire your revolver].")
        print("Firing...\n")
        sleep(2)
        print("You pull the trigger, and the bullet speeds through the air, and within less than a second, it hits the man square in the forehead, and he falls to the floor. The crowd of people go silent, and a few people jeer.\n")
        print("Suddenly, a tall, muscular man, storms up to you. 'That's my brother you just shot, you're a dead man!'")
        print("You see one of his friends yell: 'Cole is gonna wipe the floor with you!'")
        pause()
        clear()
        combat("brawl", player, cole, deadly=False)

        if player.remaining_health == 0:
            lost_brawl = True

        clear()

    clear()

    if lost_duel == False and cheated_in_duel == False:
        if lost_brawl == False:
            print("You catch your breath from the tense duel, your knuckles aching after the brawls. You look around, weighing up your next move.")
        else:
            print("You wake up a few hours later on the floor, sunlight beaming on you. Your entire body feels bruised, but you manage to get up. You look around, weighing up your next move.")
        pause()

    elif lost_duel == True:
        print("You wake up a few days later in the town doctor. You look to your right and see a small man organising a drawer of medical supplies. He notices you're awake.")
        print("\n'Oh you've woken up. I must say that was the most entertaining duel I've ever watched. It could be because of luck or skill, but I'm happy your alive.'")
        print("\nYou look down at your shoulder, which has been bandaged, but you still feel a throbbing ache.")
        print("\n'Luckily the bullet just hit your shoulder, which I've seen many times. If that bullet hit your chest or head you would've died on that street. I know I'm not your parent but you should avoid shootouts as they're known to be pretty unsafe.'")
        print("\nYou look him dead in the eyes, and he gets a bit flustered.")
        print("\n'Sorry I'll stop rambling. I will need a payment of $10 for my services though.'")
        print("\nWould you like to pay the doctor (1), try and haggle him (2), or threaten him with your revolver (3)?")
        choice3 = choice(3)

        if choice3 == "1":
            print("\nYou grudgingly pull a $10 bill from your satchel and pass it him.")
            player.money -= 10
            print(f"You now have ${player.money}")
            print("\nYou get up, clutching your shoulder before leaving.")

        elif choice3 == "2":
            print("\nYou attempt to haggle him: 'Look partner, I'm in a lot of pain and I need to find a place to sleep tonight. Could I pay you $5 instead?'")
            persuasion_result = ability_check(player, "persuasion", 12)

            if persuasion_result == "success":
                print("\nThe doctor looks at you for a second, then he sighs.")
                print("'Fine', he says. 'I guess I can do $5.'")
                print("\nYou pull a $5 bill from your satchel and pass it him.")
                player.money -= 5
                print(f"You now have ${player.money}.")
                print("\nYou get up, clutching your shoulder before leaving.")
                print("You take a deep breath of fresh air and look around, weighing up your next move.")
                pause()

            elif persuasion_result == "critical success":
                print("\nThe doctor looks at you for a second.")
                print("You know what, I had a pretty wealthy customer earlier today, you can have it for free.")
                print("\nYou thank him before leaving.")
                print("You take a deep breath of fresh air and look around, weighing up your next move.")
                pause()

            elif persuasion_result == "failure" or persuasion_result == "critical failure":
                print("\nThe doctor looks at you for a second, then he shakes his head")
                print("\n'You look more well off than me with that engraved revolver in your holster. Now pay up, and no more haggling'")
                print("\nYou grudgingly pull a $10 bill from your satchel and pass it him")
                player.money -= 10
                print(f"You now have ${player.money}.")
                print("\nYou get up, clutching your shoulder before leaving.")
                print("You take a deep breath of fresh air and look around, weighing up your next move.")
                pause()

        elif choice3 == "3":
            print("\nYou get up and point your revolver at his head.")
            print("'I wouldn't suggest making me pay if I were you'")
            print("\nThe man gulps, then he nods")
            print("\nYou put your revolver back into your holster before leaving, clutching your shoulder.")
            print("You make sure nobody saw you, then look around, weighing up your next move.")
            pause()

    elif cheated_in_duel == True:
        if lost_brawl == False:
            print("After a difficult fight you manage to knock out Cole. You wipe the sweat from your brow.")
            print("\nSuddenly you are knocked unconscious by someone behind you...")
            pause()
        clear()
        print("You wake up, your head throbbing. You look around and realise you're in a jail cell. You curse to yourself. Across the room is Sheriff Briggs, organising some files. He notices you're awake.")
        print("\n'Good, you're finally awake. I did say breaking the rules would have consequences, and those consequences are being locked here for the night. You're lucky some rancher convinced me not to hang you, or you would be dead right now. Could I have your name please?'")
        print("\nBecause of your large bounty across multiple states, you lie: 'John... Jim Milton.'")
        print("\nSheriff Briggs looks at you for a second, 'Okay John Jim Milton.' He chuckles to himself before going to his files to search them.")
        print("'I couldn't find any bounties on your name, so no payout for me. Anyway make yourself comfy because it's going to be a long night.'")
        pause()
        clear()
        print("After a relatively comfy night in the first bed you've slept in for a while, you wake up. The sheriff lets you out of your cell, and you take a deep breath of fresh air. You look around, weighing up your next move.")
        pause()

    player.remaining_health = player.max_health

def prologue():
    intro()
    duel()