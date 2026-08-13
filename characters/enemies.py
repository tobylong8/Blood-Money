from characters.player import Character

class Enemy(Character):
    def __init__(self, name, max_health, ac, attack_modifier, damage_dice, damage_modifier, initiative_modifier, attacks_per_turn=1, remaining_health=None, ai_type="balanced", dodging=False):
        if remaining_health is None:
            remaining_health = max_health

        super().__init__(
            name,
            max_health,
            remaining_health,
            ac,
            attack_modifier,
            damage_dice,
            damage_modifier,
            initiative_modifier,
            attacks_per_turn,
            dodging
        )
        self.ai_type = ai_type

cole = Enemy(
    name="Cole",
    max_health=18,
    ac=12,
    attack_modifier=4,
    damage_dice=4,
    damage_modifier=3,
    initiative_modifier=3,
    attacks_per_turn=1,
    ai_type="brute",
    dodging=False
)