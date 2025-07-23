import contextlib
import io
from pathlib import Path
import sys
import threading

import solutions.AMZ.amazing as amazing


class AmazingSolution:
    def amazing_maze(self, rows, columns, maze_generation_options):
        stdin = io.StringIO()
        stdout = io.StringIO()
        with replace_std(stdin, stdout):
            thread = threading.Thread(target = amazing.Main().run)
            thread.start()

            for line in stdout:
                line = line.rstrip()
                if not line or line.startswith(' '):
                    continue
                match line:
                    case "WHAT ARE YOUR WIDTH AND LENGTH":
                        stdin.write(f"{columns}\n")
                        stdin.write(f"{rows}\n")
                        stdin.seek(0)
                        break
                    case prompt:
                        raise Exception(f"Unknown prompt: {prompt}")

            thread.join()

            maze = [line for line in stdout if line.rstrip()]
            return "".join(maze)


def replace_std(stdin, stdout):
    return ReplaceStd(stdin, stdout)


class ReplaceStd(contextlib.AbstractContextManager):
    def __init__(self, stdin, stdout):
        self.stdin = stdin
        self.stdout = stdout

    def __enter__(self):
        self._old_stdin = sys.stdin
        self._old_stdout = sys.stdout
        sys.stdin = self.stdin
        sys.stdout = self.stdout

    def __exit__(self, _exc_type, _exc_value, _traceback):
        sys.stdin = self._old_stdin
        sys.stdout = self._old_stdout



