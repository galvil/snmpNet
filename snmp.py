#!/usr/bin/python
import sys
from interface import Interface
from router import Router
from network import Network
from easysnmp import Session


network = Network()
def polling_routers(ipRouter):

    session = Session(hostname=ipRouter, community=COMMUNITY, version=3)
    name = (session.get('SNMPv2-MIB::sysName.0'))
    router = network.getRouter(name.value)
    if router is None:
        router = Router(name.value)
    print router.getName()

def main():
    global COMMUNITY
    global ipr
    if len(sys.argv) == 3:
        ipr = sys.argv[1]
        COMMUNITY = sys.argv[2]


if __name__ == "__main__":
    main()
    polling_routers(ipr)
