from characters.player import player, Player
from characters.enemies import cole
from characters.npcs import *
from utils import *
from story_state import *
from combat import combat
from story.prologue import *

clear()
#intro()
#duel()

combat(player, cole)

input()