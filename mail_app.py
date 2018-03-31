# -*- coding: utf8 -*-

from flask import Flask
from flask_mail import Mail
from flask_mail import Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = '1105367836@qq.com'
app.config['MAIL_PASSWORD'] = '##########'
app.config['MAIL_DEFAULT_SENDER'] = '1105367836@qq.com'
# app.config['MAIL_SUPPRESS_SEND'] = True

mail = Mail(app)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/email')
def email():
    msg = Message()
    msg.add_recipient('vogtfeehily@gmail.com')

    msg.subject = 'Flask-Mail Test'
    msg.body = 'Its body!'
    # msg.html = '<b>Its html!</b>'
    import time
    start = int(time.time() * 1000)
    mail.send(msg)
    spend_time = int(time.time() * 1000) - start
    return 'Email sent, spent {} ms'.format(spend_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
