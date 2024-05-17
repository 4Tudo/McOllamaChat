# 你好! Ollama
# McOllamaChat



### 介绍
McOllamaChat是一款基于Python的ollama库和mcpi库的Minecraft聊天插件

其目的是使用简单的方式来实现Minecraft AI聊天插件

*经过测试甚至支持1.20.1*

### 使用
克隆代码

安装ollama3模型(官网下载不多做赘述 https://ollama.com/download)

下载模型
```ollama pull llama3```

安装ollama库(mcpi库是提前准备且魔改的)
```
pip install -r requirements.txt 
```

#### 设置
```settings.py```是配置文件

```chatCommand```是触发聊天机器人的指令(如果聊天中带有指令则会启动聊天)
```prompt```是模型的提示词，聊天时会采用
