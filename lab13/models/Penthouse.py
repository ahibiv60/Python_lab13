from models.House import House
 
class Penthouse(House):
    
    def __init__(self, area, price, rating, adress, number_of_rooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.number_of_rooms = number_of_rooms
        self.city = city
        
    def is_terrace(self):
        return self.terrace        
        
    def set_terrace(self, x):
        self.terrace = x