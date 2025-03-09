import subprocess
import sys

_REGISTERED_TESTS = []


def register_test():
    def decorator(func):
        _REGISTERED_TESTS.append(func)
        return func
    return decorator


def run_cli_command(script, args):
    result = subprocess.run([script] + args, capture_output=True, text=True)
    print("stdout: \n", result.stdout, end='\n')
    print("stderr: \n", result.stderr, end='\n')
    return result.returncode


def run_tests():
    all_passed = True
    for test in _REGISTERED_TESTS:
        name = test.__name__
        print(f"===========> Running {name}... <===========\n\n")
        if test() == 0:
            print(f"{name} passed!")
        else:
            all_passed = False
            print(f"{name} failed!")

    if not all_passed:
        sys.exit(1)
    print("All checks passed!")
