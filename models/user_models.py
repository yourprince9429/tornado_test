from models import Base
from sqlalchemy import Column, Integer, String
import hashlib


class User(Base):
    __tablename__ = 'student'

    # 主键自增的int类型的id主键
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 定义不能为空的唯一的姓名字段
    name = Column(String(10), nullable=False)
    age = Column(Integer, default=18)
    mobile = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)

    @classmethod
    def set_password(cls, password):
        """
        设置密码
        :param password: 用户输入的密码
        :return:
        """
        hm = hashlib.md5()
        hm.update(str(password).encode())
        return hm.hexdigest()

    def check_password(self, password):
        """
        校验密码
        :param password: 用户输入的密码
        :return:
        """
        hm = hashlib.md5()
        hm.update(str(password).encode())
        return self.password == hm.hexdigest()
