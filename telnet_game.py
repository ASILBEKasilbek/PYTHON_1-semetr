from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

class GameProtocol(LineReceiver):
    def __init__(self):
        self.score = 0

    def connectionMade(self):
        self.sendLine(b"Welcome to the Telnet Game!")
        self.sendLine(b"Press 'b' to increase your score. Type 'exit' to quit.")

    def lineReceived(self, line):
        line = line.strip().lower()
        if line == b'b':
            self.score += 1
            self.sendLine(f"Score: {self.score}".encode())
        elif line == b'exit':
            self.sendLine(b"Thanks for playing!")
            self.transport.loseConnection()
        else:
            self.sendLine(b"Invalid input. Press 'b' to increase your score or 'exit' to quit.")

class GameFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return GameProtocol()

if __name__ == '__main__':
    reactor.listenTCP(1234, GameFactory())
    print("Game server running on port 1234...")
    reactor.run()
