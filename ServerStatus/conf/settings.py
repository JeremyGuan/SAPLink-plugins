#!usr/bin/python3.4
# -*- coding:utf-8 -*-


import os

Params = {
    "server": "192.168.2.72",
    "port": 80,
    'url': '/dissona_jeesite/api/sap/server/manage',
    'request_timeout': 30,
}

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'log.log')

