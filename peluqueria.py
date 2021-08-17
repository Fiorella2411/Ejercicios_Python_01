"""Eres el analista de datos en Carly's Clippers, la peluquería más nueva de la cuadra. Su trabajo consiste en revisar las listas de datos que se han recopilado en las últimas dos semanas. Estarás calculando algunas métricas importantes que Carly puede usar para planificar el funcionamiento del negocio durante el resto del mes.

Se le han proporcionado tres listas:

hairstyles: los nombres de los cortes ofrecidos en Carly's Clippers.
prices: el precio de cada peinado de la hairstyleslista.
last_week: el número de compras para cada tipo de peinado en la última semana.
Cada índice en hairstylescorresponde a un índice asociado en pricesy last_week.

Por ejemplo, el peinado "bouffant"tiene un precio asociado de 30de la priceslista y se compró 2veces en la última semana como se muestra en la last_weeklista. Cada uno de estos elementos se encuentra en el primer índice de sus respectivas listas."""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#
total_pricey = 0
for p in prices:
  total_pricey += p
#Total de precxios de peinado
print(total_pricey)
#promedio 
average_price = total_pricey/ len(prices)
print("Average Haircut Price: ", average_price)
#nuevos precios
new_prices =[]
for p in prices:
  new_prices.append( p - 5)
print(new_prices)
#Nuevos precios metodo 2
new_prices = [price - 5 for price in prices]
print(new_prices)
#
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ", total_revenue)
#Encuentre el ingreso diario promedio dividiéndolo total_revenuepor 7. Llame a este número average_daily_revenuee imprímalo.
average_daily_revenue = total_revenue/7
print(average_daily_revenue)
#Carly cree que puede atraer más clientes anunciando todos los cortes de pelo que tiene por debajo de los 30dólares.Utilice una lista de comprensión para crear una lista llamada cuts_under_30que tenga la entrada hairstyles[i]para cada uno ipara el cual new_prices[i]es menor que 30.
cuts_under_30=[]
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
#imprimir
print(cuts_under_30)