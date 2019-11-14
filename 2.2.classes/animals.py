import math


class Animal:
    sound = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self, food_weight):
        self.weight += food_weight

    def voice(self):
        print(self.sound)


class Bird(Animal):
    def __init__(self, name, weight):
        super(Bird, self).__init__(name, weight)
        self.eggs = 0

    def laid(self):
        self.eggs += 1
        print(f'{self.name} laid an egg')

    def get_eggs(self):
        print(f'you got {self.eggs} eggs from {self.name}')
        self.eggs = 0


class Cow(Animal):
    sound = 'mouuuuuu'

    def milk(self):
        self.weight -= 10
        print(f'{self.name} gave 10 liters of milk')


class Sheep(Animal):
    sound = 'meeeeeeee'

    def shear(self):
        self.weight -= 3
        print(f'Sheared 3 kg of wool from {self.name}')


class Goat(Animal):
    sound = 'beee'

    def milk(self):
        self.weight -= 3
        print(f'{self.name} gave 3 liters of milk')


class Duck(Bird):
    sound = 'krya'


class Chicken(Bird):
    sound = 'ko-ko-ko'


class Goose(Bird):
    sound = 'ga-ga-ga'


def get_total_weight(animals):
    print('Farmer weighs animals')

    weight = 0
    for animal in animals:
        weight += animal.weight
    weight = math.floor(weight + 0.5)

    print(f'total weight of animals - {weight}')


def get_milk(animals):
    for animal in animals:
        if type(animal) == Goat or type(animal) == Cow:
            print(f'Farmer milks {animal.name}')
            animal.milk()


def laid(animals):
    for animal in animals:
        if Bird in type(animal).__mro__:
            animal.laid()


def get_eggs(animals):
    for animal in animals:
        if Bird in type(animal).__mro__:
            animal.get_eggs()


def feed_animals(animals):
    feed_for_animal = {
        Cow: 9,
        Sheep: 6,
        Goat: 5,
        Duck: 0.5,
        Goose: 0.7,
        Chicken: 0.2,
    }

    for animal in animals:
        animal.feed(feed_for_animal[type(animal)])


def get_heaviest(animals):
    max_weight = 0
    animal_name = ''
    for animal in animals:
        if animal.weight > max_weight:
            max_weight = animal.weight
            animal_name = animal.name
    print(f'The heaviest animal is {animal_name} with {max_weight} kg')


goose_1 = Goose('Серый', 13)
goose_2 = Goose('Белый', 15)
cow_1 = Cow('Манька', 150)
sheep_1 = Sheep('Барашек', 56)
sheep_2 = Sheep('Кудрявый', 64)
chicken_1 = Chicken('Ко-Ко', 3)
chicken_2 = Chicken('Кукареку', 4)
goat_1 = Goat('Рога', 36)
goat_2 = Goat('Копыта', 35)
duck_1 = Duck('кряква', 5)

animals = [goose_1, goose_2, cow_1, sheep_1, sheep_2,
           chicken_1, chicken_2, goat_1, goat_2, duck_1, ]

print('Morning is coming\n')
get_total_weight(animals)
get_milk(animals)
laid(animals)
feed_animals(animals)
get_total_weight(animals)

print('\nEvening is coming\n')
feed_animals(animals)
get_milk(animals)
get_eggs(animals)
get_total_weight(animals)
get_heaviest(animals)
print('\nGood night, my animal farm')
