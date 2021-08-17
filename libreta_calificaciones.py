"""Libro de calificaciones
Eres un estudiante y estás tratando de organizar tus asignaturas y calificaciones usando Python. Exploremos lo que hemos aprendido sobre las listas para organizar sus materias y puntuaciones."""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects =["physics","calculus","potry", "history"]
grades =[98,97,85,88]

gradebook = [["physics",98],["calculus",97], ["poetry",85],["history",88
]]
print(gradebook)
gradebook.append(["computer science", 100])
print(gradebook)
gradebook.append(["visual arts", 93])
gradebook[5][1] = 98
print(gradebook)
gradebook[2].remove(85)
print(gradebook)

gradebook[2].append("Pass")
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook
print("todas las calificaciones")
print(full_gradebook)