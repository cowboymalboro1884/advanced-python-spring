import click


@click.command()
@click.argument('input', type=click.File('r'), required=False)
def mynl(input):
    input_stream = input if input else click.get_text_stream('stdin')
    output = ""
    for line_number, line in enumerate(input_stream, start=1):
        output += f"{line_number:6}\t{line}"

    if output and not output.endswith('\n'):
        output += '\n'
    click.echo(output, nl=False)


if __name__ == "__main__":
    mynl()
