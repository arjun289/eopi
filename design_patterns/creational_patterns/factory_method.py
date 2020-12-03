from abc import ABCMeta, abstractmethod


# ------------------------- method 1 -----------------------------

class EnemyShip(metaclass=ABCMeta):
    '''Example 1 using static method in the abstract method itself '''
    @staticmethod
    def newShip(ship_type):
        if ship_type == 'Boss':
            return BossShip()
        else:
            return UFOShip()

    @abstractmethod
    def shoot(self):
        pass

    @abstractmethod
    def move(self):
        pass


class UFOShip(EnemyShip):
    def __init__(self, label="UFO"):
        self.label = label
    
    def shoot(self):
        print("UFO ship shooting")
        return

    def move(self):
        print("UFO ship moving")
        return


class BossShip(EnemyShip):
    def __init__(self, label="Boss"):
        self.label = label
    
    def shoot(self):
        print("Boss ship shooting")
        return

    def move(self):
        print("Boss ship moving")
        return


# ------------------ method 2 ----------------------------------

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def factory_method(self):
        pass

    def business_logic(self, label):
        return self.factory_method()


class ConcreteFactoryA(AbstractFactory):
    def factory_method(self):
        pass


class ConcreteFactoryB(AbstractFactory):
    def factory_method(self):
        pass


class Product(metaclass=ABCMeta):
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def name(self):
        pass


class ConcreteProductA(Product):
    def price(self):
        return 10

    def name(self):
        return "Sofa"


class ConcreteProductB(Product):
    def price(self):
        return 20

    def name(self):
        return "Chair"


# --------------------------------------------------------------------- #

if __name__ == "__main__":
    
    while(True):
        confirm = input('do you want to play(y/n): ')
        if confirm.lower() == 'y':
            result = input("Enter Ship type(Boss, UFO): ")
            result = EnemyShip.newShip(result)

            result.move()
            result.shoot()
        else:
            print("game over")
            break

