from models.House import House

class Infrastructure(House):

    def __init__(self, area, price, rating, adress, number_of_rooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.number_of_rooms = number_of_rooms
        self.city = city

    def get_is_parking(self):
        return self.is_parking        
        
    def set_is_parking(self, x):
        self.is_parking = x
        
    def get_located_near(self):
        return self.located_near        
        
    def set_located_near(self, x):
        self.located_near = x