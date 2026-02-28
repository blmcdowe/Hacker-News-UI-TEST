import subprocess
import sys
import os

def main():
    # Point directly to your test file or folder: you can run all test with this code no matter how many test cases you add to automated-ui-sorting-check.py
    project_path = "C:/your/path/PycharmProjects/PlaywrightUITests/automated-ui-sorting-check.py"
    print(f"Running tests in: {project_path}\n")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", project_path, "-s"],
        cwd=os.getcwd(),
        stdout=sys.stdout,
        stderr=sys.stderr
    )

    if result.returncode == 0:
        print("\n✅ All tests passed.")
    else:
        print("\n❌ Some tests failed.")
        sys.exit(result.returncode)

if __name__ == "__main__":

    main()
