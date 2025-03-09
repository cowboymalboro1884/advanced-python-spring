from scripts.utils import register_test, run_cli_command, run_tests


@register_test()
def run_flake8():
    return run_cli_command(script="flake8", args=["bin/", "test/", "scripts/"])


@register_test()
def run_pytest():
    return run_cli_command(script="pytest", args=["test/"])


@register_test()
def run_isort():
    args = ["--diff", "bin/", "test/", "scripts/"]
    return run_cli_command(script="isort", args=args)


def main():
    run_tests()


if __name__ == "__main__":
    main()
