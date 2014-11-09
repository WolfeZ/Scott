import socket
import time
import urllib.request
import re
 
description = '''

        +=========================================+

        |..........Scott pybot....................|

        +-----------------------------------------+

        |#desc: Scott is a free IRC both in python|

        |#Author: Rob Haverkamp                   |

        |#Date: 4/11/2014                         |

        +=========================================+

'''
print(description)
time.sleep(5)
network = 'irc.irc-chatters.net'
port = 6667
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network, port))
print(irc.recv(4096))
irc.send( b'NICK Scott\r\n' )
irc.send( b'USER Scott Scott Scott :Python s\r\n' )
time.sleep(5)
irc.send( b'JOIN #test\r\n' )
time.sleep(5)
irc.send( b'PRIVMSG #test :Hello World.\r\n')
while True:
    data = irc.recv(4096)

    if data.startswith(b'PING'):   
        irc.send(b"PONG " + data.split()[1] + b"\n")
    if data.find( b'!Scott quit' ) != -1:
      time.sleep(2)
      irc.send(b'PRIVMSG #test :Nee.\r\n' )

    if data.find(b'Scott-test') != -1:
      split_data = data.split()
      send_channel_encoded = split_data[2]
      send_channel = send_channel.decode('utf-8')
      print(send_channel, '\n')
      time.sleep(3)
      sending = irc.send('PRIVMSG {} :test\r\n'.format(send_channel).encode('utf-8'))
      print(sending)

    if data.find(b'http://') != -1:
        split_data = data.split()
        send_channel_encoded = split_data[2]
        send_channel = send_channel_encoded.decode('utf-8')
        print(send_channel, '\n')
        f = urllib.request.urlopen('http://www.python.org')
        data = f.read(6000)
        titleRE = re.compile(b"<title>(.+?)</title>")
        title = titleRE.search(data).group(1)
        print(title)
        sending = irc.send('PRIVMSG {} :{}\r\n'.format(send_channel, title).encode('utf-8'))
        print(sending)


    print(data)
