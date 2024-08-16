"""
Composition/Aggregation: has-a relationship
1. Car has a Engine
"""

class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()
        print("Car Started")

if __name__ == "__main__":
    car = Car()
    car.start()