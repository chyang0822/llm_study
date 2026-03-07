#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/6/9 18:49
@Author  : thezehui@gmail.com
@File    : 1.LLM与ChatModel使用技巧.py
"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
# 采用chatgpt大模型
# dotenv.load_dotenv()

# 设置 OpenAI API 配置
# import os
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # 替换为你的实际 API key
# # 如果使用国内代理或其他 API 端点，取消下面的注释并修改地址
# # os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"

# # 1.编排prompt
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
#     ("human", "{query}"),
# ]).partial(now=datetime.now())

# # 2.创建大语言模型
# llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# ai_message = llm.invoke(prompt.invoke({"query": "现在是几点，请讲一个程序员的冷笑话"}))

# print(ai_message.type)
# print(ai_message.content)
# print(ai_message.response_metadata)

# 采用国内阿里大模型
llm = ChatOpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen2.5-14b-instruct-1m",
    api_key="sk-3927d686315447078d6d8ef4e7ac5b9d",
)

result = llm.invoke("1+1等于多少")
print(result)
