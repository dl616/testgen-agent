import subprocess
import tempfile
import json

def run_code(code, testcases):
    print("[Agent] Running code...")

    results = []

    for case in testcases:
        input_data = case.get("input", "")
        expected = case.get("output", "")

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(code)
            filename = f.name

        try:
            process = subprocess.run(
                ["python", filename],
                input=input_data,
                text=True,
                capture_output=True,
                timeout=5
            )

            output = process.stdout.strip()

            results.append({
                "input": input_data,
                "expected": expected,
                "output": output
            })

        except Exception as e:
            results.append({
                "input": input_data,
                "expected": expected,
                "output": str(e)
            })

    return results