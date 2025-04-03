class Character:
    def __init__(self, name, health, attack_power, defence, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defence = defence
        self.speed = speed
    
    def attack(self, target):
        damage = max(1, self.attack_power - target.defence)
        target.take_damage(damage)  
        
    def take_damage(self, amount):
        self.health -= amount
        
    def is_Alive(self):
        return self.health > 0  


class Warrior(Character):
    def __init__(self, name, health, attack_power, defence, speed, rage):  
        super().__init__(name, health, attack_power, defence, speed)  
        self.rage = rage
    
    def Berserk_Mode(self):
        if self.health < 0.3 * 100: 
            self.attack_power *= 2  # Doubles attack power


class Mage(Character):
    def __init__(self, name, health, attack_power, defence, speed, mana):  
        super().__init__(name, health, attack_power, defence, speed)
        self.mana = mana

    def Fireball(self):
        pass  # Placeholder for ability logic


class Archer(Character):
    def __init__(self, name, health, attack_power, defence, speed, critical_chance):  
        super().__init__(name, health, attack_power, defence, speed)  
        self.critical_chance = critical_chance
    
    def Precision_Shot(self):
        pass 
