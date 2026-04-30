import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_requirement(problem_text):
    print("[Agent] Parsing requirement...")

    prompt = open("prompts/requirement.txt").read()

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": problem_text}
        ]
    )

    return response["choices"][0]["message"]["content"]