import socket

class IRC:
    def IRCSend(self, data):
        temp = str(data) + '\r\n'
        self.server.send(bytes(temp, 'utf-8'))
    def IRCRecv(self, size):
        return str(self.server.recv(size))
    def IRCInit(self, user, real, nick):
        self.username = user
        self.realname = real
        self.nickname = nick
        self.server = socket.socket()
        self.server.connect(('irc.nolimitzone.com', 6667))
        print('Connected')
        
        temp = 'NICK ' + nick
        self.IRCSend(bytes(temp, 'utf-8'))
        print('Nickname')
        
        temp = 'USER ' + user + ' 8 * :' + real
        self.IRCSend(bytes(temp, 'utf-8'))
        print('User')
    def IRCNick(self, nick):
        temp = 'NICK ' + nick
        self.IRCSend(bytes(temp, 'utf-8'))
    def IRCJoin(self, chan):
        temp = 'JOIN ' + chan
        self.IRCSend(bytes(temp, 'utf-8'))
        self.channel = chan
    def IRCChat(self, msg):
        temp = 'PRIVMSG ' + self.channel + ' :' + msg
        self.IRCSend(bytes(temp, 'utf-8'))
    def IRCRegister(self, email, passwd):
        temp = 'PRIVMSG NickServ :register ' + passwd + ' ' + email
        self.IRCSend(bytes(temp, 'utf-8'))
    def IRCVerifyResgister(self, nick, key):
        temp = 'PRIVMSG NickServ :verify register ' + nick + ' ' + key
        self.IRCSend(bytes(temp, 'utf-8'))
    def IRCIdentify(self, nick, passwd):
        temp = 'PRIVMSG NickServ :identify ' + nick + ' ' + passwd
        self.IRCSend(bytes(temp, 'utf-8'))
    def IRCPart(self, reason):
        temp = 'PART :' + reason
        self.IRCSend(bytes(temp, 'utf-8'))
    def IRCQuit(self, reason):
        temp = 'QUIT :' + reason
        self.IRCSend(bytes(temp, 'utf-8'))
    def __init__(self, user, real, nick):
        self.IRCInit(user, real, nick)
