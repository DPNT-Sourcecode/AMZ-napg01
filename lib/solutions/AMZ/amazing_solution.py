import os
import threading

import solutions.AMZ.amazing as amazing


class AmazingSolution:
    def amazing_maze(self, rows, columns, maze_generation_options):
        debug = open("debug.txt", "w")

        stdin_r, stdin_w = os.pipe()
        stdout_r, stdout_w = os.pipe()
        app = amazing.Main(stdin = stdin_r, stdout = stdout_w)
        thread = threading.Thread(target = app.run)
        thread.start()

        print("hello", file=debug)
        debug.flush()
        with open(stdin_w, "w") as stdin, open(stdout_r, "r") as stdout:
            for line in stdout:
                print(line, file=debug)
                debug.flush()
                line = line.rstrip()
                if not line or line.startswith(" "):
                    continue
                match line:
                    case "WHAT ARE YOUR WIDTH AND LENGTH":
                        stdin.write(f"{columns}\n")
                        stdin.write(f"{rows}\n")
                        stdin.close()
                        break
                    case prompt:
                        raise Exception(f"Unknown prompt: {prompt}")

            maze = [line for line in stdout if line.rstrip()]

            thread.join()
            return "".join(maze)


# def replace_std(stdin, stdout):
#     return ReplaceStd(stdin, stdout)


# class ReplaceStd(contextlib.AbstractContextManager):
#     def __init__(self, stdin, stdout):
#         self.stdin = stdin
#         self.stdout = stdout

#     def __enter__(self):
#         self._old_stdin = sys.stdin
#         self._old_stdout = sys.stdout
#         sys.stdin = self.stdin
#         sys.stdout = self.stdout

#     def __exit__(self, _exc_type, _exc_value, _traceback):
#         sys.stdin = self._old_stdin
#         sys.stdout = self._old_stdout


