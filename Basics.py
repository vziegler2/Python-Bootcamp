first_name = "ViKRam" #string
first_name = "ZIeGler"
print(f"Hallo {first_name.title()}")
print(f"Hallo {first_name.upper()}")
print(f"Hallo {first_name.lower()}")


x = 6 #integer
y, z = 3.5, 15.9 #float
result = y * z
print(f"Ergebnis ist: {result}")
print(x + y * z)


animals = ["Affe","Gans","Giraffe","Nashorn","Bär"] #Liste
print(animals[0])
print(animals[-2])


animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)
animals_sorted = sorted(animals)
print(f"Sortiert: {animals_sorted}")
length = len(animals)
print(f"Länge der Liste: {length}")


animals = [] #empty list
animals.append("Elefant")
animals.append("Affe")
animals.append("Nashorn")
animals.insert(1, "Gans")
print(animals)
animals.pop()
print(animals)
removedElement = animals.pop(1)
print(removedElement)
print(animals)
animals.append("Affe")
print(animals)
animals.remove("Affe")
print(animals)


cars =["Audi","BMW","VW","Mercedes"]
for x in cars:
	print(x)
counter = 0
for car in cars:
	counter += 1
	print(f"Auto Nummer: {counter} ist {car}")


digits = list(range(1,6))
for digit in digits:
	print(digit)
smallest_digit = min(digits)
print(smallest_digit)
highest_digit = max(digits)
print(highest_digit)
result = sum(digits)
print(result)


age = 16
if age < 6 or age == 6:
	print("Kostenlos")
elif age > 6 and age <= 18:
	print("Ermäßigt")
else:
	print("Vollpreis")
cities = ["Berlin","Madrid","Paris"]
if "Dortmund" in cities:
	print("Ist enthalten")
else:
	print("Nicht enthalten")


monthly_revenues = [1000,2000,3000,2500,1500,800,2200,2600,3000,2100,2000,1800]
total = sum(monthly_revenues)
total_best_months = 0
total_count_best_month = 0
for revenue in monthly_revenues:
	if revenue >= 2000:
		total_best_months += revenue
		total_count_best_month += 1
print(total_best_months)
print(f"Total revenue: {total}€, total of best months ({total_count_best_month}): {total_best_months}€")


person = {"name": "Jannick","height": 180} #Dictionary mit Key-Value-Pairs
print(person["name"])
print(f"Name ist {person['name']} und Körpergröße in cm ist {person['height']}")
persons = [
{"name": "Jannick","height": 180},
{"name": "Peter","height": 190}
]
for person in persons:
	print(f"Name ist {person['name']} und Körpergröße in cm ist {person['height']}")
person["name"] = "Viktor"
person["Freund"] = "Helmut"
person["Partner"] = {"name": "Karl","height": 170, "hasChildren": True}
print(person)
print(person["Partner"]["hasChildren"])
del person["height"]
print(person)
print(person.get("height", False))


students = {
	"Jannick" : 36335,
	"Peter" : 24543,
	"Klara" : 16423
}
for key, value in students.items():
	print(f"Key: {key} und Value: {value}")
for key in students.keys():
	print(f"Key: {key}")
for value in students.values():
	print(f"Value: {value}")
students = [
{"name": "Jannick","age": 28,"matricle_number": 35634},
{"name": "Peter","age": 30,"matricle_number": 24543},
{"name": "Xenia","age": 38,"matricle_number": 16423}
]
for student in students:
	for key, value in student.items():
		print(f"Key: {key} und Value: {value}")
count = 0
for student in students:
	count += student["matricle_number"]
print(count)