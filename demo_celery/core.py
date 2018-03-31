# -*- coding: utf8 -*-

from flask import Flask

from demo_celery.extensions import mail, celery


def create_app():
    app = Flask(__name__)

    app.config['MAIL_SERVER'] = 'smtp.qq.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USERNAME'] = '1105367836@qq.com'
    app.config['MAIL_PASSWORD'] = '########'
    app.config['MAIL_DEFAULT_SENDER'] = '1105367836@qq.com'

    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

    mail.init_app(app)
    celery.conf.update(app.config)

    return app
