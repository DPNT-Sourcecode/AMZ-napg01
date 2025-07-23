from pathlib import Path
import subprocess


class AmazingSolution:
    def __init__(self, app = Path('./amazing.py')):
        dir = Path(__file__).parent.absolute()
        self.app = dir / app

    def amazing_maze(self, rows, columns, maze_generation_options):
        with subprocess.Popen(self.app, stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = 'utf8') as process:
            while True:
                line = process.stdout.readline().rstrip()
                if not line or line.startswith(' '):
                    continue
                return line



