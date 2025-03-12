import sys

import click


def count_stats(file):
    try:
        with open(file, "rb") as f:
            content = f.read()
        lines = content.count(b"\n")
        words = len(content.split())
        bytes_count = len(content)
        return lines, words, bytes_count
    except FileNotFoundError:
        click.echo(
            f"mywc.py: cannot open '{file}' "
            "for reading: No such file or directory",
            err=True,
        )
        return None


def count_stats_stdin():
    content = sys.stdin.buffer.read()
    lines = content.count(b"\n")
    words = len(content.split())
    bytes_count = len(content)
    return lines, words, bytes_count


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=False))
def mywc(files):
    total_lines, total_words, total_bytes = 0, 0, 0

    if files:
        for file in files:
            stats = count_stats(file)
            if stats:
                lines, words, bytes_count = stats
                click.echo(f"{lines:8}{words:8}{bytes_count:8} {file}")
                total_lines += lines
                total_words += words
                total_bytes += bytes_count

        if len(files) > 1:
            click.echo(f"{total_lines:8}{total_words:8}{total_bytes:8} total")
    else:
        lines, words, bytes_count = count_stats_stdin()
        click.echo(f"{lines:8}{words:8}{bytes_count:8}")


if __name__ == "__main__":
    mywc()
