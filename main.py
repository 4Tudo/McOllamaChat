import sys
import threading
from functools import partial
sys.path.append('./mcpi')
import mcpi.minecraft as minecraft
from mcChat import *
from service import *
mc = minecraft.Minecraft.create(address='localhost')




while True:
    chat = getChat(mc)
    # print(mc.events.pollChatPosts())
    if chat[0]:
        print(chat)
        threading.Thread(target=partial(chatThread,mc=mc,msg=chat[1])).start()


