class Food:
    def __init__(self, calories):
        self.calories = calories

class Meat(Food):
    pass

class Plant(Food):
    pass

class Fruit(Food):
    pass


class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def make_sound(self):
        print(self.name, "teeb häält...")

    def eat(self, food):
        print(self.name, "sööb...")

    def get_info(self):
        return f"{self.name} ({self.__class__.__name__}): {self.age} aastat vana, {self.weight:.2f} kg"


class Lion(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    def make_sound(self):
        print(self.name, "rar!")

    def eat(self, food):
        if isinstance(food, Meat):
            print(self.name, "sööb liha.")
        else:
            print(self.name, "ei söö seda.")


class Elephant(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        
    def make_sound(self):
        print(self.name,  "uuuuu!")

    def eat(self, food):
        if isinstance(food, Plant):
            print(self.name, "sööb taimi.")
        else:
            print(self.name, "ei söö seda.")


class Monkey(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    
    def make_sound(self):
        print(self.name, "u u a a!")

    def eat(self, food):
        if isinstance(food, (Fruit, Plant, Meat)):
            print(f"{self.name} sööb {food.__class__.__name__.lower()}.")
        else:
            print(self.name, "ei söö seda.")

    def perform_trick(self):
        print(self.name, "teeb saltot!")


class Penguin(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        
    def make_sound(self):
        print(self.name, "ÄÄÄÄ!")

    def eat(self, food):
        if isinstance(food, Meat):
            print(self.name, "sööb kala.")
        else:
            print(self.name, "ei söö seda.")

    def perform_trick(self):
        print(self.name, "libiseb jääl!")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(animal.name, "lisati loomaaeda.")

    def feed_all(self, food):
        for animal in self.animals:
            animal.eat(food)

    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()

    def show_all_info(self):
        for animal in self.animals:
            print(animal.get_info())

    def make_trick_show(self):
        for animal in self.animals:
            if hasattr(animal, "perform_trick"):
                animal.perform_trick()

    def sort_by_name(self):
        self.animals.sort(key=lambda a: a.name)

    def sort_by_age(self):
        self.animals.sort(key=lambda a: a.age)

    def sort_by_weight(self):
        self.animals.sort(key=lambda a: a.weight)


zoo = Zoo()


while True:
    print("Menüü:")
    print("1. Lisa loom")
    print("2. Sööda loomi")
    print("3. Vaata loomade infot")
    print("4. Trikietendus")
    print("5. Sorteeri loomi")
    print("6. Välju programmist")
    choice = input("Vali valik: ")

    if choice == "1":
        name = input("Looma nimi: ")
        age = int(input("Vanus: "))
        weight = float(input("Kaal: "))
        print("Vali liik:\n1. Lõvi\n2. Elevant\n3. Ahv\n4. Pingviin")
        animal_choice = input("> ")

        animal = None
        if animal_choice == "1":
            animal = Lion(name, age, weight)
        elif animal_choice == "2":
            animal = Elephant(name, age, weight)
        elif animal_choice == "3":
            animal = Monkey(name, age, weight)
        elif animal_choice == "4":
            animal = Penguin(name, age, weight)

        if animal:
            zoo.add_animal(animal)
        else:
            print("Vale valik.")
    elif choice == "2":
        print("Vali toit:\n1. Liha\n2. Taim\n3. Puuvili")
        food_choice = input("> ")
        food = None
        if food_choice == "1":
            food = Meat(500)
        elif food_choice == "2":
            food = Plant(200)
        elif food_choice == "3":
            food = Fruit(300)

        if food:
            zoo.feed_all(food)
        else:
            print("Vale toiduvalik.")
    elif choice == "3":
        zoo.show_all_info()
    elif choice == "4":
        zoo.make_trick_show()
    elif choice == "5":
        print("Sorteeri loomad:\n1. Nime järgi\n2. Vanuse järgi\n3. Kaalu järgi")
        sort_choice = input("> ")
        if sort_choice == "1":
            zoo.sort_by_name()
        elif sort_choice == "2":
            zoo.sort_by_age()
        elif sort_choice == "3":
            zoo.sort_by_weight()
        zoo.show_all_info()
    elif choice == "6":
        print("Programmist väljutakse")
        break
    else:
        print("Vale valik.")
