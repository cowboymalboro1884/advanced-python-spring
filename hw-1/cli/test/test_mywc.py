import os
import subprocess
import tempfile
import unittest

from click.testing import CliRunner

from cli.bin.mywc import mywc


class TestWcSimple(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file1 = os.path.join(self.temp_dir.name, "test_file1.txt")
        self.file2 = os.path.join(self.temp_dir.name, "test_file2.txt")

        with open(self.file1, "w") as f:
            f.write("Hello world\nThis is a test file.")
        with open(self.file2, "w") as f:
            f.write("Another file\nWith more lines\nAnd words.")

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_wc_reference(self, file):
        result = subprocess.run(
            ["wc", file],
            capture_output=True,
            text=True,
        )
        return result.stdout.split()[:3]

    def test_wc_single_file(self):
        result = self.runner.invoke(mywc, [self.file1])
        expected = self.run_wc_reference(self.file1)
        actual = result.output.split()[:3]
        self.assertEqual(actual, expected)

    def test_wc_multiple_files(self):
        result = self.runner.invoke(mywc, [self.file1, self.file2])

        expected_total = (
            subprocess.run(
                ["wc", self.file1, self.file2],
                capture_output=True,
                text=True,
            )
            .stdout.splitlines()[-1]
            .split()[:3]
        )

        actual_total = result.output.splitlines()[-1].split()[:3]
        self.assertEqual(actual_total, expected_total)

    def test_wc_stdin(self):
        input_data = "Hello world\nThis is a test"
        result = self.runner.invoke(mywc, input=input_data)
        expected = subprocess.run(
            ["wc"],
            input=input_data,
            capture_output=True,
            text=True,
        ).stdout.split()[:3]
        actual = result.output.split()[:3]
        self.assertEqual(actual, expected)

    def test_wc_file_not_found(self):
        result = self.runner.invoke(mywc, ["missing_file.txt"])
        expected = "mywc.py: cannot open 'missing_file.txt' "
        "for reading: No such file or directory"
        self.assertIn(expected, result.output)


if __name__ == "__main__":
    unittest.main()
