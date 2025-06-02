import subprocess

def run_tests():
    print("Running UI tests using pytest...")
    subprocess.run(["pytest", "automated-ui-sorting-check.py", "-v"])

if __name__ == "__main__":
    run_tests()
