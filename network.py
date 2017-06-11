
class Network():
    def __init__(self):
        self.routers = list()

    def addRouter(self, router):
        if router not in routers:
            self.routers.append(router)
        else print "Error: Router already exist in the network, try with another"

    def deleteRouter(self, router):
        if router in routers:
            self.routers.remove(router)
        else print "Error: Router can not be removed because is not in the network"

    def getRouters(self):
        return self.routers

    def getRouter(self,router_name):
        for router in self.routers:
            if router.getName = router_name:
                return router
        return None
