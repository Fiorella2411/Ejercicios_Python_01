#Preserve the Verse tiene una tarea final para ti. Le han entregado una cadena que contiene una lista de poemas, titulada highlighted_poems, que quieren resaltar en el sitio, pero necesitan su ayuda para analizar la cadena en algo que pueda mostrar el nombre, título y fecha de publicación de los poemas resaltados en el sitio.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
highlighted_poems_stripped = []
print(highlighted_poems) 
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list) 

for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())
print(highlighted_poems_stripped) 

highlighted_poems_details =[]
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))
print("\n",highlighted_poems_details)

titles= []
poets = []
dates = []

for i in highlighted_poems_details:
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])
print(" ")
print(titles[1])

def favorite_song_statement(ti, po, da):
  print("The poem {} was published by {} in {}".format(ti,po,da))
for i in range(len(titles)):
  favorite_song_statement(titles[i], poets[i],dates[i])
