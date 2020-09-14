from abc import ABC,abstractmethod

class cineseleb(ABC): # abstract class
    @abstractmethod # abstract method
    def act(self):pass
    # @abstractmethod
    # def dance(self):pass
# A method without body is called abstract method
class Amithab(cineseleb):
    def act(self):
        print('Amithab is acting')

class Rajanikath(cineseleb):
    def act(self):
        print('rajanikanth is acting')

a = Amithab()
r = Rajanikath()
a.act()
r.act()

