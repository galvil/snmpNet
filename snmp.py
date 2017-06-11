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

def getInterfaces(ipRouter, rname=None):
    global network
    session = Session(hostname=ipRouter, community=COMMUNITY, version=3)
    router = network.getRouter(rname);
    ipslist = (session.walk('RFC1213-MIB::ipAdEntAddr'))

    for ip in ipslist:
        index = (session.get ('RFC1213-MIB::ipAdEntIfIndex.' + ip.value))
        name = (session.get ('IF-MIB::ifDescr.' + index.value))
        mask = (session.get('RFC1213-MIB::ipAdEntNetMask.' + ip.value))
        speed = (session.get('IF-MIB::ifSpeed.' + index.value))
        cost = (session.get ('OSPF-MIB::ospfIfMetricValue.' + ip.value))

def main():
    global COMMUNITY
    global ipr
    if len(sys.argv) == 3:
        ipr = sys.argv[1]
        COMMUNITY = sys.argv[2]


if __name__ == "__main__":
    main()
    polling_routers(ipr)
