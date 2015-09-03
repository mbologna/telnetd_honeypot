from twisted.internet import protocol, reactor, endpoints
import logging
import random

class Telnetd(protocol.Protocol):
    logging.basicConfig(filename='telnetd_honeypot.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    PROMPT = "/ # "
    def dataReceived(self, data):
        data = data.strip()
        if data == "id":
            self.transport.write("uid=0(root) gid=0(root) groups=0(root)\n")
        elif data.split(" ")[0] == "uname":
            self.transport.write("Linux f001 3.13.3-7-high-octane-fueled #3000-LPG SMPx4 Fri Jun 31 25:24:23 UTC 2200 x86_64 x64_86 x13_37 GNU/Linux\n") 
        else:
            if random.randrange(0, 2) == 0 and data != "":
                self.transport.write("bash: " +  data.split(" ")[0] + ": command not found\n")

        self.transport.write(Telnetd.PROMPT)

        if data != "":
            logging.info(self.transport.getPeer().host + " " + data)

    def connectionMade(self):
        self.transport.write(Telnetd.PROMPT)

class TelnetdFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Telnetd()

print("Listening...")
endpoints.serverFromString(reactor, "tcp:8023").listen(TelnetdFactory())
reactor.run()
