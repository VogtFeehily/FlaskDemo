# -*- coding: utf8 -*-

# from demo_celery.core import create_app  # 从这里import就无法绑定
from celery_app import create_app  # 从这里import就可以绑定.......为什么????????
from demo_celery.core import celery
# 这里的 celery import 是必要的, 因为 celery run worker 需要指定创建 celery 实例的 model

app = create_app()
app.app_context().push()
