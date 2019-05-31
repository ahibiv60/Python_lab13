from models.House import House
 
class Mansion(House):
    
    def __init__(self, area, price, rating, adress, number_of_rooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.number_of_rooms = number_of_rooms
        self.city = city
        
    def get_water_supply(self):
        return self.water_supply        
        
    def set_water_supply(self, x):
        self.water_supply = x
    
    def get_floors(self):
        return self.floors       
        
    def set_floors(self, x):
        self.floors = x