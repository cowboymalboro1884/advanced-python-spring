import subprocess
import unittest

from click.testing import CliRunner

from cli.bin.mynl import mynl


class TestMyNl(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def run_nl_reference(self, input_content):
        result = subprocess.run(
            ["nl", "-b", "a"],
            input=input_content,
            text=True,
            capture_output=True,
        )
        return result.stdout

    def test_mixed_lines(self):
        input_content = "Hello\n\nWorld\n"
        result = self.runner.invoke(mynl, input=input_content)
        expected = self.run_nl_reference(input_content)
        self.assertEqual(result.output, expected)

    def test_empty_lines(self):
        input_content = "\n\n\n"
        result = self.runner.invoke(mynl, input=input_content)
        expected = self.run_nl_reference(input_content)
        self.assertEqual(result.output, expected)

    def test_no_trailing_newline(self):
        input_content = "Line1\nLine2"
        result = self.runner.invoke(mynl, input=input_content)
        expected = self.run_nl_reference(input_content)
        self.assertEqual(result.output, expected)

    def test_empty_file(self):
        input_content = ""
        result = self.runner.invoke(mynl, input=input_content)
        expected = self.run_nl_reference(input_content)
        self.assertEqual(result.output, expected)

    def test_single_line(self):
        input_content = "Hello"
        result = self.runner.invoke(mynl, input=input_content)
        expected = self.run_nl_reference(input_content)
        self.assertEqual(result.output, expected)

    def test_special_chars(self):
        input_content = "Line\twith\ttabs\n\nLine with spaces\n"
        result = self.runner.invoke(mynl, input=input_content)
        expected = self.run_nl_reference(input_content)
        self.assertEqual(result.output, expected)

    def test_big_file(self):
        input_content = ""
        for i in range(1, 1001):
            if i % 5 == 0:
                input_content += "\n"
            else:
                input_content += f"Line {i}\n"
        result = self.runner.invoke(mynl, input=input_content)
        expected = self.run_nl_reference(input_content)
        self.assertEqual(result.output, expected)


if __name__ == "__main__":
    unittest.main()
