# MemChain
人生博物馆（MemChain）旨在为用户提供一款有温度的日记APP

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

## 环境安装

1. 基础环境：Python3.10+

2. 安装UV
```shell
pip install uv
set UV_INDEX=https://mirrors.aliyun.com/pypi/simple
```

3. 安装Python依赖包
```shell
uv sync --python 3.10 --all-extras
```

4. 切换到本地环境(.venv)
```shell
cd .venv/Scripts
activate
```

## 启动项目
1. 在conf路径中，配置系统文件`config.ini`

```text
[LLM]
base_url = https://ark.cn-beijing.volces.com/api/v3
api_key = your_api_key
model_id = deepseek-r1-250120
```

2. 启动项目的前后端

```shell
python api/memchain_server.py
python web/web_server.py
```

3. 访问项目：

系统 API 详情访问地址：http://127.0.0.1:8000/docs
用户界面访问地址：http://127.0.0.1:7860

## 开发日志
- [x] 数据库设计：[models.py](./api/db/models.py)
- [x] 日记的增删改查 API：[diaries_app.py](./api/apps/diaries_app.py)
- [x] 面向用户的日记交互网页：[web_server.py](./web/web_server.py)
- [ ] 智能分析引擎：解析用户日记，生成并存储知识图谱
- [ ] 日记管理：标签的增删改查 API（是否需要增设一张标签表？）
- [ ] 日记时间轴展示
- [ ] 本地数据加密
