from pathlib import Path
import subprocess


class AmazingSolution:
    def __init__(self, app = Path("./amazing.py")):
        dir = Path(__file__).parent.absolute()
        self.app = dir / app

    def amazing_maze(self, rows, columns, maze_generation_options):
        with subprocess.Popen(
            self.app,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            encoding = "utf8",
        ) as process:
            for line in process.stdout:
                line = line.rstrip()
                if not line or line.startswith(' '):
                    continue
                match line:
                    case "WHAT ARE YOUR WIDTH AND LENGTH":
                        process.stdin.write(f"{columns}\n")
                        process.stdin.write(f"{rows}\n")
                        process.stdin.close()
                        break
                    case prompt:
                        raise Exception(f"Unknown prompt: {prompt}")

            maze = [line for line in process.stdout if line.rstrip()]
            return "".join(maze)
