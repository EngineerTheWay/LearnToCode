#
### Define Classes
#

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def __repr__(self):
    return "-- {business} --\nLocations:\n{franchises}\n".format(business=self.name, franchises=self.franchises)

class Franchise:
  def __init__(self, name, address, menus):
    self.name = name
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "{franchise_name}\nAddress: {address}".format(franchise_name=self.name, address=self.address)

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

    #self.items_key_list = []
    #for i_name in items.keys():
      #self.items_key_list.append(i_name)

    #self.items_value_list = []
    #for i_value in items.values():
      #self.items_value_list.append(i_value)

    def calculate_bill(self, purchased_items):
      total_price = 0
      for item in purchased_items:
        total_price += item.value()
      return total_price

  def __repr__(self):
    return "{name} menu. Served from {start} to {end}.".format(name=self.name, items=self.items, start=self.start_time, end=self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
      return "Total bill: " + str(bill)

#
### Define Menus & Items
#    

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
#Create instance of brunch menu
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print(brunch_menu)

#Define early bird menu dict
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird_items, 900, 1200)
#print(early_bird_menu)

#Define dinner menu dict
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1600, 2100)
#print(dinner_menu)

#Define kids menu dict
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, 1600, 2100)
#print(kids_menu)

#Define Take a' Arepo dict
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}


#
### Calculate Menu Cost for particular items
#

#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird_menu.calculate_bill(['salumeria plate', 'vegan mushroom ravioli']))

#
### Basta Foozlin
#

## Franchises
flagship_store = Franchise("The Original Basta Foozlin'", "1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
#print(flagship_store)

new_installment = Franchise("Basta Fazoolin at Mulberry Park", "12 East Mulberry Street", [brunch_menu, dinner_menu, kids_menu])
#print(new_installment)

## Business 
basta_foozlin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#
### Take a' Arepa
#

## Franchises

arepas_place = Franchise("Take a' Arepa on Fitzgerald", "189 Fitzgerald Avenue", [arepas_menu])

## Business

take_arepa = Business("Take a' Arepa", [arepas_place])

#Test Checking available menus
#print(flagship_store.available_menus(1700))

#Test Business Class
#print(take_arepa)
#print(basta_foozlin)

