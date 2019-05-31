from models.House import House
 
class Apartment(House):
    
    def __init__(self, area, price, rating, adress, number_of_rooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.number_of_rooms = number_of_rooms
        self.city = city
        
    def get_flour(self):
        return self.flour        
        
    def set_flour(self, x):
        self.flour = x