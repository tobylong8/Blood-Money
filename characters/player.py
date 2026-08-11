class Character:
    def __init__(self, name, remaining_health, max_health, ac, attack_modifier, damage_dice, damage_modifier, initiative_modifier):
        self.name = name
        self.remaining_health = remaining_health
        self.max_health = max_health
        self.ac = ac
        self.attack_modifier = attack_modifier
        self.damage_dice = damage_dice
        self.damage_modifier = damage_modifier
        self.initiative_modifier = initiative_modifier

    def take_damage(self, amount):
        self.remaining_health -= amount
        print(f"You take {amount} damage, meaning you have {self.remaining_health}/{self.max_health} health remaining.")

    def is_dead(self):
        return self.remaining_health <= 0

    def __repr__(self):
        return self.name

class Player(Character):
    def __init__(self):
        self.name = "Jack Calloway"
        self.level = 3
        self.char_class = "Gunslinger"
        self.proficiency_bonus = 2
        self.max_health = 28
        self.ac = 13
        self.damage_dice = 6
        self.weapon = "Cattleman Revolver"
        self.money = 62

        self.strength = 12
        self.dexterity = 16
        self.constitution = 14
        self.intelligence = 8
        self.wisdom = 10
        self.charisma = 14

        self.strength_modifier = (self.strength - 10) // 2
        self.dexterity_modifier = (self.dexterity - 10) // 2
        self.constitution_modifier = (self.constitution - 10) // 2
        self.intelligence_modifier = (self.intelligence - 10) // 2
        self.wisdom_modifier = (self.wisdom - 10) // 2
        self.charisma_modifier = (self.charisma - 10) // 2

        self.initiative_modifier = self.dexterity_modifier + self.proficiency_bonus
        self.attack_modifier = self.dexterity_modifier + self.proficiency_bonus
        self.damage_modifier = self.dexterity_modifier

        self.skills = {
            "acrobatics": self.dexterity_modifier + self.proficiency_bonus,
            "animal handling": self.wisdom_modifier,
            "athletics": self.strength_modifier + self.proficiency_bonus,
            "deception": self.charisma_modifier,
            "history": self.intelligence_modifier,
            "insight": self.wisdom_modifier,
            "intimidation": self.charisma_modifier + self.proficiency_bonus,
            "investigation": self.intelligence_modifier,
            "medicine": self.wisdom_modifier,
            "nature": self.intelligence_modifier,
            "perception": self.wisdom_modifier,
            "performance": self.charisma_modifier,
            "persuasion": self.charisma_modifier + self.proficiency_bonus,
            "religion": self.intelligence_modifier,
            "sleight of hand": self.dexterity_modifier + self.proficiency_bonus,
            "stealth": self.dexterity_modifier,
            "survival": self.wisdom_modifier,
        }

        super().__init__(
            name="John Calloway",
            remaining_health=self.max_health,
            max_health=self.max_health,
            ac=self.ac,
            attack_modifier=self.attack_modifier,
            damage_dice=self.damage_dice,
            damage_modifier=self.damage_modifier,
            initiative_modifier=self.initiative_modifier
        )

player = Player()