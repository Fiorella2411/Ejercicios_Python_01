# Your code below: Trabaja en Len's Slice, una nueva pizzería en el vecindario. Utilizará su conocimiento de las listas de Python para organizar algunos de sus datos de ventas.
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas =len(toppings)
print("We sell " + str(num_pizzas)+" different kinds of pizza!")

pizza_and_prices =[[2,"pepperoni"],[6, "pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]

print(pizza_and_prices)
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza= pizza_and_prices[0]
print(cheapest_pizza)
priciest_pizza= pizza_and_prices[-1]
print(priciest_pizza)
priciest_pizza
pizza_and_prices.pop()
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)
#Tres ratones entran a la tienda. No tienen mucho dinero (son ratones), pero cada uno quiere pizzas diferentes.
three_cheapest = pizza_and_prices[:3]
print(three_cheapest )