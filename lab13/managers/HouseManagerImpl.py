class HouseManagerImpl:
    house_list = []
    
    @staticmethod
    def get_list():
        return HouseManagerImpl.house_list

    @staticmethod
    def sort_by_area(is_reversed):
        HouseManagerImpl.house_list.sort(key=lambda house: house.area, reverse=is_reversed)
            
    @staticmethod    
    def sort_by_price(is_reversed):
        HouseManagerImpl.house_list.sort(key=lambda house: house.price, reverse=is_reversed)
            
    @staticmethod    
    def set_new_list_of_houses(houses):
        HouseManagerImpl.house_list = houses
    
    @staticmethod
    def clear_houses():
        HouseManagerImpl.house_list.clear()
    
    @staticmethod
    def add_house(house):
        HouseManagerImpl.house_list.append(house)
    
    @staticmethod
    def print_list_of_houses():
        for v in HouseManagerImpl.house_list:
            print("adress: %s, city: %s\n" % (v.get_adress, v.get_city))
            
    @staticmethod
    def find_house_by_city(city_to_find):
        return list(filter(lambda house: house.city == city_to_find, HouseManagerImpl.house_list))