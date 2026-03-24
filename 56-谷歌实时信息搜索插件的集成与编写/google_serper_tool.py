#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/7/8 16:53
@Author  : thezehui@gmail.com
@File    : google_serper_tool.py
"""
import json
import os
from typing import Any, Type

import dotenv
import requests
from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool

dotenv.load_dotenv()


class GoogleSerperArgsSchema(BaseModel):
    query: str = Field(description="执行谷歌搜索的查询语句")


class GoogleSerperTool(BaseTool):
    """使用 Google Serper API 进行实时谷歌搜索"""
    name: str = "google_serper"
    description: str = "一个低成本的谷歌搜索API，当你需要回答有关时事的问题时可以调用该工具，输入为搜索查询语句"
    args_schema: Type[BaseModel] = GoogleSerperArgsSchema

    def _run(self, *args: Any, **kwargs: Any) -> str:
        """根据传入的查询语句调用 Google Serper API 进行搜索"""
        try:
            # 1.获取 Serper API 秘钥
            serper_api_key = os.getenv("SERPER_API_KEY")
            if not serper_api_key:
                return "Google Serper API 秘钥未配置"

            # 2.从参数中获取查询语句
            query = kwargs.get("query", "")
            if not query:
                return "查询语句不能为空"

            # 3.调用 Google Serper API
            response = requests.post(
                url="https://google.serper.dev/search",
                headers={
                    "X-API-KEY": serper_api_key,
                    "Content-Type": "application/json",
                },
                data=json.dumps({"q": query, "gl": "cn", "hl": "zh-cn"}),
            )
            response.raise_for_status()
            data = response.json()

            # 4.提取搜索结果并返回
            results = []
            # 提取知识图谱摘要
            if "knowledgeGraph" in data:
                kg = data["knowledgeGraph"]
                results.append(f"知识图谱：{kg.get('title', '')} - {kg.get('description', '')}")
            # 提取 answerBox 直接答案
            if "answerBox" in data:
                ab = data["answerBox"]
                answer = ab.get("answer") or ab.get("snippet", "")
                results.append(f"直接答案：{answer}")
            # 提取有机搜索结果
            for item in data.get("organic", [])[:5]:
                title = item.get("title", "")
                snippet = item.get("snippet", "")
                link = item.get("link", "")
                results.append(f"标题：{title}\n摘要：{snippet}\n链接：{link}")

            if results:
                return "\n\n".join(results)
            return f"未找到关于 '{query}' 的搜索结果"

        except Exception as e:
            return f"搜索 '{kwargs.get('query', '')}' 时发生错误：{str(e)}"


google_serper = GoogleSerperTool()
result = google_serper.invoke({"query": "2024年巴黎奥运会中国代表团共获得几枚金牌"})
print(result)
