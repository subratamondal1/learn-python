from abc import ABC, abstractmethod

# Interface for mammals that can swim
class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

# Interface for mammals that can run
class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass

# A dolphin can swim but can't run
class Dolphin(Swimmable):
    def swim(self):
        print("Dolphin is swimming")

# A cheetah can run but can't swim
class Cheetah(Runnable):
    def run(self):
        print("Cheetah is running")

# Example usage
dolphin = Dolphin()
cheetah = Cheetah()

dolphin.swim()  # Output: Dolphin is swimming
cheetah.run()   # Output: Cheetah is running
