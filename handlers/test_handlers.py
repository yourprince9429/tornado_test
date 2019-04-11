from .base import BaseHandler

# 定义视图
class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("<h1>hello tornado</h1>")
