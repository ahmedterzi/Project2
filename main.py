class Faction:
    def __init__(self, name, number_of_units, health_point,attack_point, unit_regeneration_number):
        self.name = name
        self.number_of_units = number_of_units
        self.health_point = health_point
        self.attack_point = attack_point
        self.unit_regeneration_number = unit_regeneration_number
        self.total_health = self.number_of_units * self.health_point
        self.is_alive = True
    def AssgnEnemies(self, first_enemy, second_enemy):
        self.first_enemy = first_enemy
        self.second_enemy = second_enemy
    def PerformAttack(self):
        try:
            if  self.first_enemy .is_alive ==True and self.second_enemy.is_alive == True:
                self.first_enemy.ReceiveAttack(self, (self.attack_point/10)*5)
                self.second_enemy.ReceiveAttack(self, (self.attack_point/10)*5)
            elif self.first_enemy.is_alive ==True and self.second_enemy.is_alive == False:
                self.first_enemy.ReceiveAttack(self, self.attack_point)
            elif self.first_enemy.is_alive ==False and self.second_enemy.is_alive == True:
                self.second_enemy.ReceiveAttack(self, self.attack_point)
            else:
                pass
        except AttributeError:
            print('Before calling this function, use AssgnEnemies function and assign enemies to function')