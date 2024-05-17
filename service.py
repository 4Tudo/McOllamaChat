import ollama
from ollama import Client
import re

import settings



client = Client(host='http://localhost:11434')

def getChatContent(msg):
  response = client.chat(model='llama3', messages=[
    {
      'role': 'user',
      'content': msg,
      'prompt': settings.prompt,
    },
  ])
  print(response)
  return response['message']['content']



def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

# ————————————————
#
# 版权声明：本文为博主原创文章，遵循
# CC
# 4.0
# BY - SA
# 版权协议，转载请附上原文出处链接和本声明。
#
# 原文链接：https: // blog.csdn.net / weixin_45459224 / article / details / 105855545
def chatThread(mc,msg):
    print('Started generating!')
    stream = client.generate(
        model='llama3',
        prompt=msg,
        system=settings.prompt,
        # messages=[{'role': 'user', 'content': msg,'prompt': settings.prompt}],
        stream=True,
    )
    streamList = ''
    for chunk in stream:
        streamList += str(chunk['response']).replace('\n', '')
        streamList = filter_emoji(streamList)
        print(filter_emoji(chunk['response']),end='',flush=True)
        try:
            mc.postToChat(f'{" "*3000}{streamList}')
        except Exception as e:
            print(f'Error content:', chunk['response'])
            print(f'Generating error!: {e}')
    print('Generate complete!')

# print(getChatContentStream('你好!'))
