name = input("Bitte gib deinen Namen ein: ")
print(f"Name ist {name}")
number_as_string = input("Bitte gib eine Zahl ein: ")
y = int(number_as_string) + 10
print(y)
number_as_float = float(number_as_string)
input("Drücke eine Taste zum beenden")


cars = ["BMW","Audi","Mercedes","Volkswagen","Toyota"]
user_car = input("Nach welchem Auto suchst du? ")
if user_car in cars:
	print(f"Wir haben einen {user_car} gefunden!")
else:
	print(f"Wir haben keinen {user_car} gefunden!")


animal = {"name": "","type": "","age": 0}
animal["name"] = input("Bitte gib den Namen des Tieres ein: ")
animal["type"] = input("Bitte gib den Typ des Tieres ein: ")
animal["age"] = int(input("Bitte gib das Alter des Tieres ein: "))
print(animal)