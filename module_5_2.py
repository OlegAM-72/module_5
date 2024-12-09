class House:
    def __init__(self, name, number_of_floors):  #не смог найти где Опечатка в методе __init__:
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return self.name

    def __len__(self):
         return self.number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 1 <= new_floor <= self.number_of_floors:  # исправления с прошлого задания
            for i in range(new_floor):
                print(i+1)
        else:
            print("Такого этажа не существует")

h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
h1.go_to(1)