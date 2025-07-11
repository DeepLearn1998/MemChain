import configparser
import os.path

from api.utils.project_path import get_project_path

# 实例化配置文件
config = configparser.ConfigParser()
CONFIG_PATH = os.path.join(get_project_path(), 'conf', 'config.ini')


def load_app() -> tuple:
    """
    获取 APP 相关配置
    :return: host，port
    """
    with open(CONFIG_PATH, 'r', encoding='utf-8') as config_file:
        config.read_file(config_file)
    host = config['APP']['host']
    port = int(config['APP']['port'])
    return host, port


def load_database() -> str:
    """
    获取数据库相关配置
    :return: 数据库信息
    """
    with open(CONFIG_PATH, 'r', encoding='utf-8') as config_file:
        config.read_file(config_file)
    database_connection = config['DATABASE']['sqlite_connection']
    return database_connection


def load_llm() -> tuple:
    """
    获取 LLM 相关配置
    :return: URL，密钥，模型名称
    """
    with open(CONFIG_PATH, 'r', encoding='utf-8') as config_file:
        config.read_file(config_file)
    base_url = config['LLM']['base_url']
    api_key = config['LLM']['api_key']
    model_id = config['LLM']['model_id']
    return base_url, api_key, model_id


def load_prompt(user_input=None, task=None) -> str:
    """
    组织系统提示词 system_prompt
    :param user_input: 用户输入
    :param task: 任务类型
    :return: 系统提示词
    """
    # 获取配置文件
    with open(CONFIG_PATH, 'r', encoding='utf-8') as config_file:
        config.read_file(config_file)
    # 获取系统提示词
    if task == 'knowledge_graph':
        return config['PROMPT']['knowledge_graph'].format(question=user_input)  # 接下来需要考虑如何让输出更可控，符合json格式
    else:
        return config['PROMPT']['system_prompt']


if __name__ == '__main__':
    print(load_app())
    print(load_database())
    print(load_llm())
