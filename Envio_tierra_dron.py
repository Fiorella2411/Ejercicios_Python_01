'''Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
Here are the prices:'''
weight = 41.8
cost_ground =""
cost_drone =""
#Envio Terreste
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  # more calculation
  cost_ground = weight * 3 + 20
elif weight <= 10:
  # more calculation
  cost_ground = weight * 4 + 20
else:
  # last calculation
  cost_ground = weight * 4.75 + 20

#impriminedo resultados
print(cost_ground)
cost_ground_premium = 125.00
print("Ground Shipping Premimium $", cost_ground_premium)
print("Costo por Tierra: ", cost_ground_premium + cost_ground)

#Envio en DRONES
if weight <= 2:
  cost_drone = weight * 4.5 
elif weight <= 6:
  # more calculation
  cost_drone = weight * 9
elif weight <= 10:
  # more calculation
  cost_drone = weight * 12
else:
  # last calculation
  cost_drone = weight * 14.25
#impriminedo resultados
print("Costo por dron", cost_drone)

