import gradio as gr
import requests


# FastAPI 服务 URL
BASE_URL = "http://127.0.0.1:8000/diaries"


def create_diary(title: str, content: str):
    """创建日记"""
    try:
        response = requests.post(
            BASE_URL + "/",
            json={
                "title": title,
                "content": content,
                "weather": "晴",
                "location": {"lat": 0, "lng": 0},
                "tags": ["学习"],
                "mood": "开心",
                "mood_score": 100
            }
        )
        return f"创建成功！日记ID：{response.json()['id']}"
    except Exception as e:
        return f"创建失败：{str(e)}"


def search_diary(diary_id: int):
    """查询日记"""
    try:
        response = requests.get(f"{BASE_URL}/{diary_id}")
        if response.status_code == 404:
            return "未找到该日记"
        if response.status_code == 200:
            data = response.json()
            return f"""标题：{data.get('title','')}\n内容：{data.get('content','')}"""
    except requests.exceptions.HTTPError:
        return "未找到该日记"


def update_diary(diary_id: int, title: str, content: str):
    """更新日记"""
    try:
        requests.put(
            f"{BASE_URL}/{diary_id}",
            json={"title": title, "content": content}
        )
        return "更新成功！"
    except Exception as e:
        return f"更新失败：{str(e)}"


def delete_diary(diary_id: int):
    """删除日记"""
    try:
        response = requests.delete(f"{BASE_URL}/{diary_id}")
        if response.status_code == 404:
            return "未找到该日记"
        if response.status_code == 200:
            return response.json()["message"]
    except Exception as e:
        return f"删除失败：{str(e)}"


with gr.Blocks() as demo:
    gr.Markdown("# MemChain 📔——日记管理系统")

    with gr.Row(equal_height=True):
        # 增加/删除日记
        with gr.Column():
            # 创建区块
            gr.Markdown("## 新建日记")
            title_input = gr.Textbox(label="标题")
            content_input = gr.Textbox(label="内容", lines=5)
            create_btn = gr.Button("保存日记")
            create_output = gr.Textbox(label="操作结果")
            # 删除区块
            gr.Markdown("## 删除日记")
            delete_id = gr.Number(label="要删除的日记ID")
            delete_btn = gr.Button("删除日记")
            delete_output = gr.Textbox(label="删除结果")

        # 查询/修改日记
        with gr.Column():
            # 查询区块
            gr.Markdown("## 查询/修改日记")
            search_id = gr.Number(label="输入日记ID")
            search_btn = gr.Button("查询日记")
            search_output = gr.Textbox(label="日记内容", lines=4)
            # 修改区块
            new_title = gr.Textbox(label="新标题")
            new_content = gr.Textbox(label="新内容", lines=4)
            update_btn = gr.Button("更新日记")
            update_output = gr.Textbox(label="更新结果")

    # 事件绑定
    create_btn.click(
        create_diary,
        inputs=[title_input, content_input],
        outputs=create_output
    )

    search_btn.click(
        search_diary,
        inputs=search_id,
        outputs=search_output
    )

    update_btn.click(
        update_diary,
        inputs=[search_id, new_title, new_content],
        outputs=update_output
    )

    delete_btn.click(
        delete_diary,
        inputs=delete_id,
        outputs=delete_output
    )

demo.launch(share=True)
