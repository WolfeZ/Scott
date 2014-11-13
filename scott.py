import socket
import time
import urllib.request
import re

intro = '''

        +=========================================+

        |..........Scott pybot....................|

        +-----------------------------------------+

        |#desc: Scott is a free IRC both in python|

        |#Author: Rob Haverkamp                   |

        |#Date: 4/11/2014                         |

        +=========================================+

'''
print(intro)

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enc = 'utf-8'
readbuffer = ''


def irc_connect(server='', port=0):
    while 1:
        try:
        
            port = int(port)
            irc.connect((server, port))
            print(irc.recv(1024))
            break
        except socket.error:
            print('Something went wrong...')
            exit(0)

def irc_join(channel='', nickname=''):
    while 1:
        print(irc.recv(1024))
        
        try:
            irc.send('NICK Scott'.encode(enc))
            irc.send('USER Scott Scott irc.irc-chatters.net :Scott \r\n'.encode(enc))
            irc.send('JOIN #test'.encode(enc))
            time.sleep(10)
            irc.send('PRIVMSG {} :Hello World.\r\n'.format(channel).encode(enc))
            print(irc.recv(1024))
            break
        except socket.error:
            print('something went wrong..')
            exit(0)

#def channel(message):
            
    
        
        
nickname = 'Scott'
irc_connect('irc.irc-chatters.net', 6667)
irc_join('#test', 'Scott')

while 1:

  msg = irc.recv(2048) 
  msg = msg.strip(b'\n\r')
  if msg.startswith(b'PING'):
      msg.send(b"PONG " + data.split()[1] + b"\n")
  print(msg)
  break

exit(0)


