from managers.HouseManagerImpl import HouseManagerImpl
from models.Mansion import Mansion
from models.Penthouse import Penthouse
from models.Apartment import Apartment

def main():
    h = HouseManagerImpl()

    house1 = Mansion(155, 11465432, 5, 'Warsaw, 5', 6, 'Lviv')
    house2 = Penthouse(136, 2383150, 4, 'Charles Michelosh, 7', 4, 'Kiev')
    house3 = Apartment(100, 530400, 3, 'Solomyanska, 20A', 2, 'Odessa')
    h.add_house(house1)
    h.add_house(house2)
    h.add_house(house3)

    h.print_list_of_houses()
    print("."*20)
    print("Sort area by descending\n")
    h.sort_by_area(True)
    h.print_list_of_houses()
    print("."*20)
    print("Sort price by ascending\n")
    h.sort_by_price(False)
    h.print_list_of_houses()
    print("."*20)
    print("House in Lviv: ", h.find_house_by_city('Lviv'))

if __name__ == "__main__": main()
