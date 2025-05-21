from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.config_load import load_database


engine = create_engine(load_database(), connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """数据库会话管理生成器函数，用于依赖注入"""
    # 创建数据库会话实例
    db = Session()
    try:
        yield db  # yield 将会话提供至请求
    finally:
        db.close()  # 关闭会话
