#!usr/bin/python3.4
# -*- coding:utf-8 -*-

import json
import time
import urllib.parse
import urllib.request
from core import info_collection
from conf import settings


class ArgvHandler(object):

    def __init__(self, args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        if len(self.args) > 1 and hasattr(self, self.args[1]):
            func = getattr(self, self.args[1])
            func()
        else:
            self.help_msg()

    @staticmethod
    def help_msg():
        msg = '''
            show_data   显示数据
            report_data 提交数据
        '''
        print(msg)

    @staticmethod
    def show_data():
        info = info_collection.InfoCollection()
        ip = info.get_ip()
        print(ip)

    @staticmethod
    def report_data():
        """
        获取本机IP地址,然后发送至服务器
        :return:
        """
        # 获取IP
        info = info_collection.InfoCollection()
        ip = info.get_ip()
        url = "http://%s:%s%s?serverType=%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'], ip)
        print('正在将数据发送至： [%s]  ......' % url)

        try:
            response = urllib.request.urlopen(url=url, data=None, timeout=settings.Params['request_timeout'])
            message = str(response.read(), 'utf-8')
            j = json.loads(message)
            retstatus = j['resultMsg']['status']
            print('返回结果: %s ' % retstatus)
        except Exception as e:
            message = '发送失败'
            print("发送失败，%s" % e)
        with open(settings.PATH, 'ab') as f:
            string = '发送时间：%s \t 服务器地址：%s \t 返回结果：%s \n' % (time.strftime('%Y-%m-%d %H:%M:%S'), url, retstatus)
            f.write(string.encode())
            print("日志记录成功！")


