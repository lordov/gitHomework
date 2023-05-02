# Welcome user.
print("""
#======================================#
| Добро пожаловать в классный журнал!  |
| Введите сначала имя ученника         |
| потом введите его оценку.            |
| Чтобы узнать среднюю оценку всех     |
| введенных учеников, введите пустое   |
| значение.                            |
#======================================#
""")
# Empty dictonary for values.
school_class = {}
# Ask the name of the student. 
name = input("Enter the student's name: ")

while name != "":

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        print("Enter the right score")
        break
    # Adding the keys and scores to the dictonary, if the keys in dictonary adding only scores.
    scores = school_class.get(name, [])
    scores.append(score)
    school_class.update({name: scores})
    name = input("Enter the student's name: ")


# Calculate average scores and output the values. 
for name in sorted(school_class.keys()):
    print(name,':', sum(school_class[name]) / len(school_class[name]))
