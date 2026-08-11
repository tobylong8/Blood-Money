from random import randint
from time import sleep
from characters.player import *
from characters.enemies import *
from characters.npcs import *
from utils import *
from combat import *
import pyfiglet

def intro():
    print("=" * 65 + "\n")
    print(pyfiglet.figlet_format("BLOOD     MONEY", font="smslant"))
    print("=" * 65) 
    print("\n")
    print("Blood Money is a text-based western adventure with Dungeons and Dragons mechanics.")
    print("You will make choices, roll dice, and live with the consequences.\n")
    print("To make a choice, type the corresponding number and press enter.")
    print("Some choices will trigger ability checks — the outcome depends on your stats and the roll of a dice.\n")
    print("You play as John Calloway, an infamous outlaw and hired gun with the best shot in the state.")
    print("And the last man who should ever trust a stranger buying him a drink.\n")
    input("Would you like to start the game (1), or get a quick overview of the mechanics (2)?")
    choice1 = choice(2)
    if choice1 == "2":
        # Mechanics overview
        print("")
    print("\n")

def duel():
    print("June 7th, 1872. You stand in hot summer sun, facing a large, angry man on the other side of the street. You lock eyes, gripping your holsters, and you feel a bead of sweat drip from your brow. There's a hushed crowd, and you see a mother cover her boy's eyes.")
    print("\n'I'm sending you straight to hell!' He shouts, his mean eyes staring intensely into yours.\n")
    
    print("Would you like to antagonise him (1), persuade him not to fight (2), or not respond (3)?")
    choice1 = choice(3)
    if choice1 == "1":
        print("\nYou respond, wiping the barrel of your revolver with a cloth. 'Last feller that talked to me like that ain't talkin' no more.'")
        intimidation_result = ability_check(player, "intimidation",12)
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
            print("\nAs you attempt to intimidate him, your voice breaks slightly. You see the man cackle to himself, and a few members of the crowd join in. 'This might me the funniest duel I have ever done.' The man says, before chuckling some more.")
            print("Your embarrassment causes you to have disadvantage in the duel.\n")
            print("'I feel kinda bad that I'm about to kill you now.' He says, still smiling.\n")    
    elif choice1 == "2":
        print("\nYou attempt to persuade him, 'Come on now, there's no need to fight. It was just a joke.'")
        persuasion_result = ability_check(player, "persuasion",15)
        if persuasion_result == "success" or persuasion_result == "critical success":
            print("\n'Guess we shouldn't fight with the kids around' He says, his angry expression fading.")
            print("Suddenly, you see his friend slap him. 'What the hell has gotten into you, you're just going to let him get away with insultin' your mother!'")
            print("He remains silent for a few seconds, before his angry expression returns. 'You better start singing your prayers you damn bastard.'\n")
        elif persuasion_result == "failure":
            print("\nYou see that his angry expression isn't gone.")
            print("'It's too late now to apologize now you damn cocksucker!' He shouts, furiously looking at you.\n")
        elif persuasion_result == "critical failure":
            print("\nAfter your attempt to persuade him, he looks furious. He points his revolver to the sky and shoots. You see people stand back.")
            print("'IF YOU THINK YOU CAN BE A GODDAMN COWARD AFTER INSULTING MY MOTHER, THEN YOU CAN GO AND SHOOT YOURSELF!'\n")    
    elif choice1 == "3":
        print("\nYou remain silent, staring itently into his eyes. He stays quiet after that.\n")
    pause()
    print("\nA few tense seconds of silence pass, where the only thing you hear is the howling wind. Eventually, the silence is broken when the man says: 'When is this duel gonna start goddamnit?'\n")
    print("A tall man wearing a long, brown coat with a silver star pinned to his chest steps from the crowd, 'Hello gentlemen, I'm Sheriff Briggs. I'll be overseeing this duel, and I want to see a fair game from both of you.'\n")
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
                print("\nYou dive to the side, dodging the bullet. While lying down, you point your revolver at the man's head.")
                input("[Press enter to fire your revolver].")
                print("Firing...\n")
                sleep(2)
                print("You pull the trigger, and the bullet speeds through the air, and within less than a second, it hits the man square in the forehead. He falls to the floor, a gaping wound spewing blood. The crowd of people go silent. You get up from the ground and put your revolver back in your holster")
                # Bar
            elif dive == "failure":
                print("You try and dive but it is too late. The bullet goes straight into your left shoulder.\n")
                player.take_damage(randint(3,5))
                print("You lay on the ground for a few seconds, clutching your shoulder. Several bullets narrowly miss you. Through the constant ringing, you hear the man yell about running out of ammo. You hear sprinting footsteps coming towards you. You turn towards him, and you see him running full force with a knife in his hand. You point the revolver at his head.")
                input("[Press enter to fire your revolver].")
                print("Firing...\n")
                sleep(2)
                print("Through the nauseating pain, you pull the trigger, and the bullet speeds through the air, and within less than a second, it hits the man square in the forehead. He falls to the floor, a gaping wound spewing blood. The crowd of people go silent. You put your revolver back in your holster, your left hand pressed tight against your bullet wound.\n")
                pause()
                print("You begin to feel dizzy, and you fall unconscious.")
                # Hospital
        else:
            print("You pull the trigger, and the bullet speeds through the air, and within less than a second, it hits the man square in the forehead. He falls to the floor, a gaping wound spewing blood. The crowd of people go silent, then you hear hushed whispers. You put your revolver back in your holster.\n")
            # Bar
    elif choice2 == "2":
        print("\nThe sheriff continues counting. You see your opponent gripping his holster, anxiously waiting for when he says 10. You lock eyes, like a predator staring down its prey.")
        print("A few more seconds pass, but before the sheriff says 10, you take out your revolver.\n")
        input("[Press enter to fire your revolver].")
        print("Firing...\n")
        sleep(2)
        print("You pull the trigger, and the bullet speeds through the air, and within less than a second, it hits the man square in the forehead. He falls to the floor. The crowd of people go silent, and a few people jeer.\n")
        print("Suddenly, a tall, muscular man, storms up to you. 'That's my brother you just shot, you're a dead man!'")
        print("You see one of his friends yell: 'Thomas is gonna wipe the floor with you!'")

