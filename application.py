import os
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
from urls import urls
from config.config import configs
from tornado.options import define, options

define("port", type=int, default=9001)
define("host", type=str, default='0.0.0.0')

options.log_file_prefix = os.path.join(os.path.dirname(__file__), 'logs/tornado_main.log')


class CustomApplication(tornado.web.Application):
    # 定义初始化方法
    def __init__(self, urls, configs):
        handlers = urls
        settings = configs
        super(CustomApplication, self).__init__(handlers=handlers, **settings)


# 格式化日志输出格式
# 默认是这种的：[I 160807 09:27:17 web:1971] 200 GET / (::1) 7.00ms
# 格式化成这种的：[2016-08-07 09:38:01 执行文件名:执行函数名:执行行数 日志等级] 内容消息
class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

# 定义工厂方法
def create_app():
    tornado.options.parse_command_line()
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    http_server = tornado.httpserver.HTTPServer(CustomApplication(urls, configs))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    return http_server
