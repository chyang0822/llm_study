#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""

@Time    : 2024/6/28 17:13

@Author  : thezehui@gmail.com

@File    : 1.faiss向量数据库使用示例.py

"""

import dotenv

from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings



dotenv.load_dotenv()



embedding = OpenAIEmbeddings(

    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

    model="text-embedding-v4",

    api_key="sk-3927d686315447078d6d8ef4e7ac5b9d",

    # 添加额外的配置以兼容阿里云API

    check_embedding_ctx_length=False

    )


# 示例文本数据

texts = [

    "笨笨是一只很喜欢睡觉的猫咪",

    "我喜欢在夜晚听音乐，这让我感到放松。",

    "猫咪在窗台上打盹，看起来非常可爱。",

    "学习新技能是每个人都应该追求的目标。",

]



# 创建并保存 Faiss 向量数据库

db = FAISS.from_texts(texts, embedding)

db.save_local("./23-Faiss向量数据库的配置与使用/vector-store")



# 或者加载已存在的数据库（如果已经创建过）

# db = FAISS.load_local("./23-Faiss向量数据库的配置与使用/vector-store", embedding, allow_dangerous_deserialization=True)



print(db.similarity_search_with_score("我养了一只猫，叫笨笨"))

