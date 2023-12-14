from abc import ABC, abstractmethod

# Define an abstraction for a food source
class FoodSource(ABC):
    @abstractmethod
    def provide_food(self):
        pass

# Define a concrete implementation of the food source
class Grass(FoodSource):
    def provide_food(self):
        return "grass"

# Define another concrete implementation of the food source
class Meat(FoodSource):
    def provide_food(self):
        return "meat"

# High-level module that depends on the food source abstraction
class Mammal:
    def __init__(self, food_source: FoodSource):
        self.food_source = food_source

    def eat(self):
        food = self.food_source.provide_food()
        print(f"This mammal eats {food}")

# Example usage
cow = Mammal(Grass())
lion = Mammal(Meat())

cow.eat()  # Output: This mammal eats grass
lion.eat()  # Output: This mammal eats meat