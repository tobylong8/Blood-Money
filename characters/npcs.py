from characters.player import Character

class NPC(Character):
    def __init__(self, name, remaining_health, max_health, ac, attack_modifier, damage_dice, damage_modifier):
        self.name = name
        super().__init__(remaining_health, max_health, ac, attack_modifier, damage_dice, damage_modifier)