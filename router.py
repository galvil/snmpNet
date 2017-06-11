#!/usr/bin/python
#from netaddr import IPNetwork

class Router:
    def __init__(self, name):
        self.name = name
        self.routerinterfaces = list()
        self.connected = list()
        self.routeTable = list()

    def rename(self,name):
        self.name = name

    def getName(self):
        return self.name

    def addInterface(self, interface):
        if interface not in routerinterfaces:
            self.routerinterfaces.append(interface)
        else: print "Error: Interface is already connected, try with another"

    def deleteInterface(self,interface):
        if interface in routerinterfaces:
            self.routerinterfaces.remove(interface)
        else: print "Error: Interface is not connected with this router, try with another"

    def getInterfaces (self):
        return self.routerinterfaces

    def addRouterConnected (self, router):
        if router not in connected:
            self.connected.append(router)
        else: print "Error: Router is already connected, try with another"

    def deleteRouterConnected(self,router):
        if router in connected:
            self.connected.remove(router)
        else: print "Error: Router is not connected with this router, try with another"

    def addNewRoute (slef, route):
        if route not in routeTable:
            self.routeTable.append(route)

    def getRouteTable(self):
        return self.routeTable
