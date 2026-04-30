from agents.requirement_agent import parse_requirement
from agents.testcase_agent import generate_testcases
from agents.execution_agent import run_code
from agents.validation_agent import validate
from agents.fix_agent import fix_code

def main():
    problem = open("examples/sample_problem.txt").read()
    code = open("examples/sample_code.py").read()

    req = parse_requirement(problem)
    tests = generate_testcases(req)

    max_retry = 3

    for i in range(max_retry):
        print(f"\n=== Iteration {i+1} ===")

        results = run_code(code, tests)
        report = validate(results)
        print(report)

        # 判断是否全部通过
        if "Failed: 0" in report:
            print("✅ All tests passed!")
            break
        else:
            print("❌ Tests failed, fixing code...")
            code = fix_code(code, results)

    print("\nFinal Code:\n")
    print(code)

if __name__ == "__main__":
    main()
