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
    def ReceiveAttack(self, enemy, point):
        if enemy == self.first_enemy:
            point = point
        else:
            point = point
        if self.total_health <= 0:
            self.is_alive = False
            print('The faction was destroyed')
        elif point > self.total_health:
            self.total_health = 0
            self.is_alive = False
            print('The faction was destroyed')
        else:
            self.total_health = self.total_health -point
        self.number_of_units = self.total_health / self.health_point

    def PurchaseWeapons(self, point_wanted, merchant):
        self.attack_point += point_wanted
        merchant.revenue += point_wanted
        merchant.weapon_point -= point_wanted
    def PurchaseArmors(self, point_wanted, merchant):
        self.health_point += point_wanted
        merchant.revenue += point_wanted
        merchant.weapon_point -= point_wanted
    def Print(self):
        return self.__dict__
    def EndTurn(self):
        if self.number_of_units <= 0:
            self.number_of_units = 0
            self.is_alive = False
        else:
            pass
        self.number_of_units += self.unit_regeneration_number
        self.total_health = self.number_of_units * self.health_point
class Merchant:
    def __init__(self, starting_weapon_point, starting_armor_point):
        self.weapon_point = starting_weapon_point
        self.armor_point = starting_armor_point
        self.starting_weapon_point = starting_weapon_point
        self.starting_armor_point = starting_armor_point
        self.revenue = 0