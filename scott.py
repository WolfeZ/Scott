import socket
import time
 
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
      splitted = data.split()
      send_channel = splitted[2]
      decoded = send_channel.decode('utf-8')
      print(decoded, '\n', splitted)
      if decoded == 'Scott':
          continue
      else:
          time.sleep(3)
          sending = irc.send('PRIVMSG {} :test\r\n'.format(decoded).encode('utf-8'))
          print(sending)


    print(data)
