from sqlalchemy import create_engine
from utils.config_load import load_database
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine(load_database(), pool_size=5, max_overflow=10)


def get_db():
    """依赖注入创建数据库会话"""
    # 创建数据库会话实例
    db = scoped_session(sessionmaker(bind=engine))
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
