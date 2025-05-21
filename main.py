from fastapi import FastAPI
from models import Base
from database import engine
from routers import diaries
import uvicorn
from utils.config_load import load_app


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
