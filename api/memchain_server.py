import os

import uvicorn
from fastapi import FastAPI

from api.apps import diaries_app as diaries
from api.db.database import engine
from api.db.models import Base
from api.utils.config_load import load_app

# 创建数据库文件目录（新增代码）
os.makedirs(os.path.dirname(engine.url.database), exist_ok=True)
# 创建数据库表
Base.metadata.create_all(bind=engine)
# 实例化 FastAPI
app = FastAPI()
app.include_router(diaries.router)


@app.get("/")
def read_root():
    return {"message": "欢迎使用智能日记本 MemChain"}


def main():
    host, port = load_app()
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
