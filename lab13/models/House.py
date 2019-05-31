import os

class House():

    def __init__(self, area, price, rating, adress, number_of_rooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.number_of_rooms = number_of_rooms
        self.city = city

    def __repr__(self):
        return repr((self.area, self.price, self.rating, self.adress, self.number_of_rooms, self.city))

    @property
    def get_area(self):
        return self.area

    def set_area(self, x):
        self.area = x

    @property
    def get_price(self):
        return self.price

    def set_price(self, x):
        self.price = x

    @property
    def get_rating(self):
        return self.rating

    def set_rating(self, x):
        self.rating = x

    @property
    def get_adress(self):
        return self.adress

    def set_adress(self, x):
        self.adress = x

    @property
    def get_number_of_rooms(self):
        return self.number_of_rooms

    def set_number_of_rooms(self, x):
        self.number_of_rooms = x

    @property
    def get_city(self):
        return self.city

    def set_city(self, x):
        self.city = x

def main():
	print('work!')
if __name__ == "__main__": main()

os.system("PAUSE")
