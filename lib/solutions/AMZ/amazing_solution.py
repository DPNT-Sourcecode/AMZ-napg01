from pathlib import Path
import subprocess


class AmazingSolution:
    def __init__(self, app = Path('./amazing.py')):
        self.app = app.absolute()

    def amazing_maze(self, rows, columns, maze_generation_options):
        subprocess.Popen(self.app, stdin = subprocess.PIPE, stdout = subprocess.PIPE)

