from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.db.database import get_db
from api.db.models import Diary
from api.models.schemas import DiaryResponse, DiaryCreate, DiaryUpdate

router = APIRouter(prefix="/diaries", tags=["diaries"])


@router.post("/", response_model=DiaryResponse)
def create_diary(diary: DiaryCreate, db: Session = Depends(get_db)) -> Diary:
    """
    新增日记
    :param diary: 日记模型 DiaryCreate
    :param db: 数据库会话
    :return: Diary
    """
    db_diary = Diary(**diary.dict(),
                     created_at=datetime.utcnow(),  # 添加创建时间
                     updated_at=datetime.utcnow()  # 添加更新时间
                     )
    db.add(db_diary)
    db.commit()
    db.refresh(db_diary)
    return db_diary


@router.get("/{diary_id}", response_model=DiaryResponse)
def read_diary(diary_id: int, db: Session = Depends(get_db)):
    """
    搜索日记
    :param diary_id: 日记 id
    :param db: 数据库会话
    :return: Diary
    """
    # 根据 id 查询日记，并返回第一条记录
    diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if not diary:
        raise HTTPException(status_code=404, detail="日记不存在")
    return diary


@router.put("/{diary_id}", response_model=DiaryResponse)
def update_diary(
        diary_id: int,
        diary_update: DiaryUpdate,
        db: Session = Depends(get_db)
):
    """
    更新日记
    :param diary_id: 日记id
    :param diary_update: 日记模型 DiaryCreate
    :param db: 数据库会话
    :return: Diary
    """
    db_diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if not db_diary:
        raise HTTPException(status_code=404, detail="日记不存在")

    for key, value in diary_update.dict().items():
        if value is not None and value != "":
            setattr(db_diary, key, value)

    db.commit()
    db.refresh(db_diary)
    return db_diary


@router.delete("/{diary_id}")
def delete_diary(diary_id: int, db: Session = Depends(get_db)):
    """
    删除日记
    :param diary_id: 日记 id
    :param db: 数据库会话
    :return: 删除结果
    """
    diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if not diary:
        raise HTTPException(status_code=404, detail="日记不存在")

    db.delete(diary)
    db.commit()
    return {"message": "日记删除成功"}
