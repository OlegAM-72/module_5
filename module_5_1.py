class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 1 < new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i+1)
        else:
            print("Такого этажа не существует")

h1 = House('ЖК "Домосед"', 9)
h1.go_to(8)

