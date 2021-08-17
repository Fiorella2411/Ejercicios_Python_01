#articulo  descripcion y precio 1
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254
#articulo  descripcion y precio 2
stylish_settee_description ="Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50
#articulo  descripcion y precio 3
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

sales_tax = .088

#primer cliente
customer_one_total = 0 
customer_one_itemization = ""

#Un cliente compraea un Lovely Loveseat
customer_one_total += lovely_loveseat_price
print(customer_one_total)
customer_one_itemization += lovely_loveseat_description + "************"
# cliente decidio comprart una lampara luxurius
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description + "************"
# Tiempo de pagar calculando impuestos
customer_one_tax = customer_one_total * sales_tax
#Total a pagar
customer_one_total += customer_one_tax

#Imprimiendo Resultados
print("Customer One Items:"+ customer_one_itemization)
print("Customer One Total:"+ str(customer_one_total))