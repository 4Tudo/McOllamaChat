import settings

def getChat(mc):
    try:
        chatContent = mc.events.pollChatPosts()[0].message
        if settings.chatCommand in chatContent:
            return [True,chatContent.replace(settings.chatCommand, '')]
        else:
            return [False, '']
    except Exception:
        return [False, '']

