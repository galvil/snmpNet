#!/usr/bin/python
import sys
from interface import Interface
from router import Router
from network import Network
from easysnmp import Session

def polling_routers(ipRouter):
    global network
    session = Session(hostname=ipRouter, community=COMMUNITY, version=2)
    name = (session.get('SNMPv2-MIB::sysName.0'))
    print name

def main():
    global COMMUNITY
    global ipr
    if len(sys.argv) == 3:
        ipr = sys.argv[1]
        COMMUNITY = sys.argv[2]


if __name__ == "__main__":
    main()
    polling_routers(ipr)
