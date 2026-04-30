def validate(results):
    print("[Agent] Validating results...")

    passed = 0

    for r in results:
        if str(r["expected"]).strip() == str(r["output"]).strip():
            passed += 1

    total = len(results)

    report = f"""
==== Test Report ====
Total: {total}
Passed: {passed}
Failed: {total - passed}
====================
"""

    return report