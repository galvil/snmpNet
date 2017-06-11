
class Interface:
    def __init__(self, name, ipAddress, mask, speed, cost):

        self.name = name
        self.ipAddress = ipAddress
        self.mask = mask
        self.speed = speed
        self.cost = cost

        def changeIpAddresAndMask(self, ipAddress,mask):
            self.ipAddress = ipAddress
            self.mask = mask

        def getIpAddress(self):
            return self.ipAddress

        def getMask(self):
            return self.mask

        def getSpeed(self):
            return self.speed

        def getCost(self):
            return self.cost

        def changeCost(self, cost):
            self.cost = cost
