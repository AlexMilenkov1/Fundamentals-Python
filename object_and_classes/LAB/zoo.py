class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, searched_species):
        if searched_species == 'mammal':
            return f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"

        elif searched_species == 'fish':
            return f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"

        elif searched_species == 'bird':
            return f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


name_of_zoo = input()
number_of_lines = int(input())

zoo = Zoo(name_of_zoo)

for _ in range(number_of_lines):
    info = input().split()

    type_animal, animal = info

    zoo.add_animal(type_animal, animal)

special_species = input()

print(zoo.get_info(special_species))
