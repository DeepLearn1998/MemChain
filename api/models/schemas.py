from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional

from pydantic import BaseModel, Field, field_validator


class MoodEnum(str, Enum):
    happy = "开心"
    sad = "难过"
    excited = "激动"


class DiaryCreate(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., max_length=2000)
    weather: str = Field(..., max_length=20)
    location: Dict[str, float]  # {"lat": float, "lng": float}
    tags: List[str]
    mood: str  # 允许自由输入，但推荐使用枚举值
    mood_score: int = Field(..., ge=0, le=100)

    @classmethod
    @field_validator("mood")
    def mood_must_be_valid(cls, v):
        """校验 mood 字段"""
        allowed = ["开心", "难过", "激动"]
        if v not in allowed:
            print(f"警告：非预设情绪 '{v}'，已允许自由输入")
        return v


# 新增更新专用模型
class DiaryUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    weather: Optional[str] = None
    location: Optional[Dict[str, float]] = None
    tags: Optional[List[str]] = None
    mood: Optional[str] = None
    mood_score: Optional[int] = None


class DiaryResponse(DiaryCreate):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]
