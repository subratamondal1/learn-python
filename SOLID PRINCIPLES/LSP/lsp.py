### LISKOV SUBSTITUTION PRINCIPLE ###

# Violates LSP
class Mammal:
    def can_give_birth(self):
        print("I can give birth to live young.")

class Dog(Mammal):
    def can_give_birth(self):
        print("I can give birth to puppies.")

class Platypus(Mammal):
    def can_give_birth(self):
        print("I lay eggs instead of giving birth to live young.")


# Follows LSP
class Mammal:
    def reproduce(self):
        print("I reproduce in a way that is typical for mammals.")

class Dog(Mammal):
    def reproduce(self):
        print("I give birth to puppies.")

class Platypus(Mammal):
    def reproduce(self):
        print("I lay eggs.")
