from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Diary(Base):
    """ORM"""
    __tablename__ = "diaries"  # 表名

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)  # 主键，自增长
    user_id: Mapped[int] = mapped_column(Integer, default=1)  # 用户ID，默认为1
    title: Mapped[str] = mapped_column(String(100))  # 日记标题
    content: Mapped[str] = mapped_column(String(2000))  # 日记内容
    # 创建时间 server_default=func.now() 设置默认值为当前时间
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    # 更新时间 onupdate=func.now() 自动记录数据最后一次更新时间
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())
    weather: Mapped[str] = mapped_column(String(30))  # 天气
    location: Mapped[dict] = mapped_column(JSON())  # 位置的经纬度坐标 {"lat": 31.23, "lng": 121.47} 后续需结合高德API确认一遍
    tags: Mapped[dict] = mapped_column(JSON())  # 标签 ["旅行", "家庭"]
    mood: Mapped[str] = mapped_column(String(30))  # 心情
    mood_score: Mapped[str] = mapped_column(Integer)  # 情绪得分


if __name__ == "__main__":
    # 查看 Diary 中的属性
    print(Diary.__table__)
