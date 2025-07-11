from openai import OpenAI

from api.utils.config_load import load_llm


def deepseek_reasoner(system_prompt: str) -> str:
    """
    通过 API 调用 deepseek-r1
    :param system_prompt: 系统提示词
    :return: LLM 回复
    """
    # 加载配置文件
    base_url, api_key, model_id = load_llm()
    # 调用 LLM
    client = OpenAI(base_url=base_url, api_key=api_key)
    completion = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "system", "content": system_prompt}],
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    print(deepseek_reasoner("你是谁？"))
