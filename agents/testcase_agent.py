import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_testcases(requirement):
    print("[Agent] Generating testcases...")

    prompt = open("prompts/testcase.txt").read()

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": requirement}
        ]
    )

    content = response["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        print("⚠️ JSON解析失败，返回空测试集")
        return []