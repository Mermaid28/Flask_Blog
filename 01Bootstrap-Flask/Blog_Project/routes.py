#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
# @Project ：Bootstrap-Flask 
# @File    ：routes.py
# @IDE     ：PyCharm 
# @Author  ：A30041699
# @Date    ：2024/10/10 14:38
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5

from .forms import LoginForm


# 首先创建了一个 Flask 应用，并且设置了一个名为 ‘SECRET_KEY’ 的配置项，这个配置项用于启用所有 Flask 和某些其扩展的加密功能
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = "123456"  # 或者 app.secret_key = '123456'

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title="Home")


@app.route('/about')
def about():
	return render_template('about.html', title="About")


# 在 routes.py 文件中定义一个路由，以处理表单的提交和页面的渲染
# 定义了一个名为 login 的视图函数。这个函数首先创建了一个 LoginForm 实例，然后检查这个表单是否通过了所有的验证（即所有的字段都已填写）。
# 如果表单通过了验证，我们会显示一条消息，然后重定向到登录页。否则，我们会渲染登录模板，并将表单传递给模板。
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	# form.validate_on_submit()是Flask-WTF扩展提供的一个方便的方法，它将处理表单提交的所有事务。
	# 当你在视图函数中调用form.validate_on_submit()，它将会做两件事：
	# 1.它首先检查请求方法是否是 POST 或 PUT，这两种方法常常用于提交表单。在 HTTP 协议中，GET 请求通常用于获取数据，而 POST 和 PUT 请求通常用于提交数据。
	# 2.如果请求方法是 POST 或 PUT，那么 validate_on_submit() 进一步调用 form.validate() 来运行每个字段的验证器。
	# 这些验证器是在你的 Form 类中定义的（例如在 LoginForm 中的 DataRequired）。如果所有的字段都通过了验证，form.validate() 将返回 True，否则返回 False。
	# 所以，如果 form.validate_on_submit() 返回 True，那么这意味着客户端发起了一个 POST 或 PUT 请求，且所有的字段都已填写（通过验证）。这是提交表单的一个常见模式。
	if form.validate_on_submit():
		flash('Login requested for user {}, remember={}'.format(form.username.data, form.remember.data))
		return redirect(url_for('login'))
	return render_template('login.html', title='Sign In', form=form)