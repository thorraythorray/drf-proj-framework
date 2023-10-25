# -*- coding: utf-8 -*-
import multiprocessing
import pathlib
import os

LOG_PATH = '/var/log/avator'
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

workers = max(2, min(int(multiprocessing.cpu_count() / 2) + 1, 5))
bind = '127.0.0.1:9002'
# bind = '0.0.0.0:9002'
worker_class = 'gevent'

threads = 2
worker_connections = 1000
max_requests = 2000
keepalive = 2
timeout = 300
graceful_timeout = 30

reload = True
debug = False
daemon = False  # 启动后台进程（当supervisor管理进程时需要False)

# pidfile = '/run/phthisis.pid'
chdir = str(pathlib.Path().parent.resolve())
loglevel = 'info'
errorlog = f'{LOG_PATH}/gunicorn_error.log'
accesslog = f'{LOG_PATH}/gunicorn_access.log'