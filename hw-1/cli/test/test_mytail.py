import os
import subprocess
import tempfile
import unittest

from click.testing import CliRunner

from cli.bin.mytail import mytail


class TestTailSimple(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file1 = os.path.join(self.temp_dir.name, "test_file1.txt")
        self.file2 = os.path.join(self.temp_dir.name, "test_file2.txt")
        with open(self.file1, "w") as f:
            f.write("".join([f"Line {i}\n" for i in range(1, 12)]))
        with open(self.file2, "w") as f:
            f.write("A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL")

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_tail_reference(self, file, lines=10):
        result = subprocess.run(
            ["tail", "-n", str(lines), file],
            capture_output=True,
            text=True,
        )
        return result.stdout

    def test_tail_single_file(self):
        result = self.runner.invoke(mytail, [self.file1])
        expected = self.run_tail_reference(self.file1)
        self.assertEqual(result.output.strip(), expected.strip())

    def test_tail_multiple_files(self):
        result = self.runner.invoke(mytail, [self.file1, self.file2])

        expected = (
            f"==> {self.file1} <==\n"
            f"{self.run_tail_reference(self.file1)}"
            f"\n"
            f"==> {self.file2} <==\n"
            f"{self.run_tail_reference(self.file2)}"
        )

        self.assertEqual(result.output.strip(), expected.strip())

    def test_tail_stdin(self):
        input_data = "\n".join(str(i) for i in range(1, 21))
        result = self.runner.invoke(mytail, input=input_data)

        expected = subprocess.run(
            ["tail", "-n", "17"],
            input=input_data,
            capture_output=True,
            text=True,
        ).stdout

        self.assertEqual(result.output.strip(), expected.strip())

    def test_tail_file_not_found(self):
        result = self.runner.invoke(mytail, ["missing_file.txt"])
        expected = "mytail.py: cannot open 'missing_file.txt' "
        "for reading: No such file or directory"
        self.assertIn(expected, result.output)


if __name__ == "__main__":
    unittest.main()
