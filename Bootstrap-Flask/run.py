#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
# @Project ：Bootstrap-Flask 
# @File    ：run.py
# @IDE     ：PyCharm 
# @Author  ：A30041699
# @Date    ：2024/10/10 14:42
from Blog_Project import app

# 创建一个run.py来启动应用
if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1', port=3000)