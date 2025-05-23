# MemChain
人生博物馆（MemChain）旨在为用户提供一款有温度的日记APP
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

## 环境配置

- Python >= 3.10
- 安装依赖：[requirements.txt](./requirements.txt)
- 修改配置：[config.ini](./config.ini)

## 项目结构
```
/MemChain
├── llm
|   └── llm_api.py    # API 调用 LLM
├── routers
|   └── diaries.py    # 日记相关路由
├── utils
|   ├── config_load.py    # 从配置文件中加载数据
|   └── project_path.py    # 定位项目根目录，即 MemChain 文件夹
├── config.ini    # 配置文件
├── database.py    # 数据库配置
├── diaries.db    # SQLite 数据库
├── main.py    # APP 入口
├── models.py    # ORM 定义数据模型
├── README.md    # 说明文档
├── requirements.txt    # 依赖需求
└── schemas.py    # Pydantic 模型
```

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
