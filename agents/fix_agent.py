import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def fix_code(code, test_results):
    print("[Agent] Fixing code...")

    prompt = f"""
You are a code fixing agent.

The following code has errors based on test results.

Code:
{code}

Test Results:
{test_results}

Fix the code so that all test cases pass.

Return ONLY the fixed code.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You fix Python code."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]