from sqlalchemy import create_engine
# 继承Student的基类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 连接数据库的配置文件
# 连接数据库格式
# mysql+pymysql://root:root@127.0.0.1:3306/tornado9
db_url = 'mysql+pymysql://root:mysql@127.0.0.1:3306/my_tornado'

# 创建引擎，建立连接
engine = create_engine(db_url)

# 模型与数据库表进行关联的基类,模型必须继承与Base
Base = declarative_base(bind=engine)

# 创建session会话
DbSession = sessionmaker(bind=engine)
db = DbSession()
