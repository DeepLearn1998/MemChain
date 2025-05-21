from pathlib import Path


def get_project_path():
    """获取项目根目录"""
    current_file = Path(__file__).resolve()
    return current_file.parent.parent


if __name__ == '__main__':
    print(get_project_path())
