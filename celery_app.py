# -*- coding: utf8 -*-

from demo_celery.core import create_app
from demo_celery.tasks import add, send_email


app = create_app()


@app.route('/')
def index():
    add.delay(10, 20)
    return 'Hello World'


@app.route('/email')
def email():
    send_email.delay()
    return 'Email sent asynchronously'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
