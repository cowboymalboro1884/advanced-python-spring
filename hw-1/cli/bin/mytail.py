import sys

import click


def tail(file, lines=10):
    try:
        with open(file, "r") as f:
            content = f.readlines()
        return "".join(content[-lines:])
    except FileNotFoundError:
        click.echo(
            f"mytail.py: cannot open '{file}' for reading: No such file or directory",
            err=True,
        )
        return None


def tail_stdin(lines=17):
    content = sys.stdin.readlines()
    return "".join(content[-lines:])


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=False))
def main(files):
    if files:
        for i, file in enumerate(files):
            if len(files) > 1:
                click.echo(f"==> {file} <==")
            output = tail(file)
            if output:
                click.echo(output, nl=True)
    else:
        click.echo(tail_stdin(), nl=False)


if __name__ == "__main__":
    main()
