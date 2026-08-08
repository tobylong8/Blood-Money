from characters.player import Character

class Enemy(Character):
    def __init__(self, remaining_health, max_health, ac, attack_modifier, damage_dice, damage_modifier):
        super().__init__(remaining_health, max_health, ac, attack_modifier, damage_dice, damage_modifier)

enemy_brother = Enemy(18, 18, 12, 4, 4, 3)