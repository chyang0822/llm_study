#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/7/13 12:34
@Author  : thezehui@gmail.com
@File    : 2.LLM文生图应用.py
"""
import dotenv
from langchain_community.tools.openai_dalle_image_generation import OpenAIDALLEImageGenerationTool
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

dalle = OpenAIDALLEImageGenerationTool(api_wrapper=DallEAPIWrapper(model="dall-e-3"))

llm = ChatOpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen2.5-14b-instruct-1m",
    api_key="sk-3927d686315447078d6d8ef4e7ac5b9d",
)
llm_with_tools = llm.bind_tools([dalle], tool_choice="openai_dalle")

chain = llm_with_tools | (lambda msg: msg.tool_calls[0]["args"]) | dalle

print(chain.invoke("帮我绘制一张老爷爷爬山的图片"))
