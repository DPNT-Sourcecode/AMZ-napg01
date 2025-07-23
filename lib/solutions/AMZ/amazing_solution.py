from pathlib import Path
import subprocess


class AmazingSolution:
    def __init__(self, app = Path('./amazing.py')):
        dir = Path(__file__).parent.absolute()
        self.app = dir / app

    def amazing_maze(self, rows, columns, maze_generation_options):
        with subprocess.Popen(self.app, stdin = subprocess.PIPE, stdout = subprocess.PIPE) as process:
            for line in process.stdout.readlines():
                return line


