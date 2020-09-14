from abc import ABC, abstractmethod

class tatacars(ABC):

    @abstractmethod
    def addGps(self):
        """
        Implement this
        :return:
        """
        pass

    def addRearCam(self):
        """
        Implement this
        :return:
        """
        pass
    def m1(self):
        print('print m1')

class tatanano(tatacars):
    def addGps(self):
        print('gps added')

car1 = tatanano()
car1.m1()