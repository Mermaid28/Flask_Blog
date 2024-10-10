#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
# @Project ：Bootstrap-Flask 
# @File    ：forms.py
# @IDE     ：PyCharm 
# @Author  ：A30041699
# @Date    ：2024/10/9 11:13
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

# 在forms.py中创建表单的定义
# 定义了一个名为 LoginForm 的类，它代表登录表单。这个表单有三个字段：username 和 password，remember
# 这两个字段都使用了 DataRequired 验证器，意味着这两个字段是必填的。在表单的最后，我们还定义了一个 submit 字段，它是一个提交按钮。
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')