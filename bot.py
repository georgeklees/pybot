# -*- coding: utf-8 -*-
import irc, os, sys, time, platform, easygui
from ctypes import c_int, WINFUNCTYPE, windll
from ctypes.wintypes import HWND, LPCSTR, UINT

masternick = ''
cmdflag = False
chanflag = True
channel = input('Enter a channel to go to: ').strip()
thebot = irc.IRC('MN1Bot', 'MN1Bot', 'MN1Bot')
thebot.IRCJoin(channel)
while True:
    mydat = str(thebot.IRCRecv(4096))
    print(mydat)
    if 'PING' in mydat:
        print("PINGPONG")
        thebot.IRCSend('PONG')
    if 'PRIVMSG KickBot :sekritpass' in mydat:
        pmflag = True
        for i in range(0, len(mydat)):
            if mydat[i] == ':':
                continue
            if mydat[i] == ':':
                masternick = mydat[:i]

        thebot.IRCSend('PRIVMSG Marionumber1 :You are now the commander of me!')
    if masternick + ' PRIVMSG KickBot :$chanon' in mydat and pmflag:
        thebot.IRCChat('Marionumber1 has turned on channel commands')
        chanflag = True
    if masternick + ' PRIVMSG KickBot :$chanoff' in mydat and pmflag:
        thebot.IRCChat('Marionumber1 has turned off channel commands')
        chanflag = False
    if 'PRIVMSG ' + channel + ' :$say' in mydat and chanflag:
        for i in range(0, len(mydat)):
            if mydat[i] == '$':
                thebot.IRCChat(mydat[i + 5:])
                break
    if masternick + ' PRIVMSG KickBot :$say' in mydat and pmflag:
        for i in range(0, len(mydat)):
            if mydat[i] == '$':
                thebot.IRCChat(mydat[i + 5:])
                break
    if 'PRIVMSG ' + channel + ' :$kick' in mydat and chanflag:
        kicknick = mydat.split(' PRIVMSG ' + channel + ' :$kick')[0]
        if 'Marionumber1' in kicknick:
            thebot.IRCChat('Marionumber1 can\'t be kicked')
        else:
            thebot.IRCSend('KICK ' + channel + ' ' + kicknick.split('!')[0])
    if masternick + ' PRIVMSG KickBot :$kick' in mydat and pmflag:
        for i in range(0, len(mydat)):
            if mydat[i] == '$':
                kicknick = mydat[i + 6:]
                if kicknick == 'Marionumber1':
                    thebot.IRCChat('Marionumber1 can\'t be kicked')
                    break
                else:
                    thebot.IRCSend('KICK ' + channel + ' ' + kicknick)
                    break
    if masternick + ' PRIVMSG KickBot :$raw' in mydat and pmflag:
        for i in range(0, len(mydat)):
            if mydat[i] == '$':
                thebot.IRCSend(mydat[i + 5:])
                break
    if masternick + ' PRIVMSG KickBot :$quit' in mydat and pmflag:
        thebot.IRCChat('Ciao!')
        sys.exit()


             

        
        
    
    
