from characters.player import Character

class Enemy(Character):
    def __init__(self, name, remaining_health, max_health, ac, attack_modifier, damage_dice, damage_modifier, initiative_modifier):
        super().__init__(
            name,
            remaining_health,
            max_health,
            ac,
            attack_modifier,
            damage_dice,
            damage_modifier,
            initiative_modifier
        )

enemy_brother = Enemy(
    name="Thomas",
    remaining_health=18,
    max_health=18,
    ac=12,
    attack_modifier=4,
    damage_dice=4,
    damage_modifier=3,
    initiative_modifier=3
)