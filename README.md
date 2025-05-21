# MemChain

## 环境配置

- Python >= 3.10
- [requirements.txt](./requirements.txt)

## 用户配置
- [config.ini](./config.ini)

## 启动项目
```shell
conda create -n MemChainEnv python=3.10
cd path/to/MemChain
pip install -r requirements.txt
python main.py
```
浏览器访问：[API 文档](http://127.0.0.1:8000/docs)

## 开发日志
- [x] 数据库设计：[models.py](./models.py)
- [x] 日记的增删改查 API：[diaries.py](./routers/diaries.py)
- [ ] 智能分析引擎：解析用户日记，生成并存储知识图谱
- [ ] 日记管理：标签的增删改查 API（是否需要增设一张标签表？）
- [ ] 日记时间轴展示
- [ ] 本地数据加密