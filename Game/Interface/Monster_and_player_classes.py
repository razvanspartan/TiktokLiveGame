class Player:
    def __init__(self, attack, health_current, health_max, image, level):
        self.attack = attack
        self.health_current = health_current
        self.health_max = health_max
        self.level = level
        self.image = image

    def attackUpgrade(self, target):
        self.attack = attack+1

    def healthUpgrade(self):
        self.health_max = health_max+1

    def heal(self, health_amount):
        self.health_current += health_amount

    def take_damage(self, damage):
        self.health_current -= damage
        if self.health_current < 0:
            self.health_current = 0

class Monster1:
    def __init__(self, attack, health_current, health_max,image):
        self.attack = attack
        self.health_current = health_current
        self.health_max = health_max
        self.image = image

    def heal(self, health_amount):
        self.health_current += health_amount

    def take_damage(self, damage):
        self.health_current -= damage
        if self.health_current < 0:
            self.health_current = 0
