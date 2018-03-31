# -*- coding: utf8 -*-
from flask_mail import Message

from demo_celery.core import celery
from demo_celery.core import mail


@celery.task
def add(x, y):
    result = x + y
    return result


@celery.task
def send_email():
    msg = Message()
    msg.add_recipient('vogtfeehily@gmail.com')

    msg.subject = 'Flask-Mail & Celery Test'
    msg.body = 'Its body!'
    mail.send(msg)
