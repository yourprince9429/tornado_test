import tornado.web
import json
from models import db


class BaseHandler(tornado.web.RequestHandler):
    """
    基本接口处理对象
    """
    model_obj = None  # 模型类对象

    def initialize(self):
        # 创建Session的对象，将MainHandler的对象传入
        # self.my_session = Session(self)
        self.db = db
        if self.model_obj:
            self.query_set = self.db.query(self.model_obj)

    def get(self):
        user_id = self.get_argument('id')
        user = self.query_set.filter(self.model_obj.id == user_id).first()
        data = {
            "name": user.name,
            "age": user.age,
            "mobile": user.mobile
        }
        self.finish(data)
        # self.return_json(data)


    def return_json(self, data):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json.dumps(data))
        self.finish()
