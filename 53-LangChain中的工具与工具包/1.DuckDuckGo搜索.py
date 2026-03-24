#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/7/8 11:08
@Author  : thezehui@gmail.com
@File    : 1.DuckDuckGo搜索.py
"""
import dotenv

dotenv.load_dotenv()

# DuckDuckGo 在国内服务器无法访问，改用 Tavily 搜索
# 需要先在 https://tavily.com 注册获取免费 API key
# 并在 .env 文件中设置 TAVILY_API_KEY=your-key
from langchain_tavily import TavilySearch

search = TavilySearch(max_results=3)
result = search.invoke("LangChain的最新版本是什么?")
print(result)
print("名字：", search.name)
print("描述：", search.description)
print("参数：", search.args)
print("是否直接返回：", search.return_direct)
