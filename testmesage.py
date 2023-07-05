from Message import *
from time import sleep

Message.send("Hi", None,None)
Message.send("How are you?", None,None)
Message.send("Malaka!", None,None)

sleep(1)


print(Message.all[0].body )
sleep(1)
print(Message.all[0].body )

print(Message.all[0].created )
print(Message.all[0].viewed )
