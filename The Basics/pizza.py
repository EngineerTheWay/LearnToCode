#Define pizza slices with their prices
from cmath import pi

#Define lists
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

#Number of pizzas and types
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

#advertise 
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#print(pizza_and_prices) check the list

#sort numerically
pizza_and_prices.sort()

#most exenpsive pizza
priciest_pizza = pizza_and_prices[-0]

#remove anchovies
pizza_and_prices.pop()

#add peppers
pizza_and_prices.insert(4, [2.5, "peppers"])

#select 3 cheapest pizzas
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)